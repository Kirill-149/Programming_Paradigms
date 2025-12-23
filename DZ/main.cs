using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace PerformanceMonitor
{
    // ==================== ИНТЕРФЕЙСЫ ====================

    public interface IPerformanceMetric<T> where T : struct
    {
        string? Name { get; }
        T CurrentValue { get; }
        DateTime? LastUpdated { get; }
        Task UpdateAsync(CancellationToken cancellationToken = default);
    }

    // ==================== МЕТРИКИ ====================

    public sealed class CpuUsageMetric : IPerformanceMetric<double>
    {
        private readonly Random _random = new();
        private double _currentValue;
        private DateTime? _lastUpdated;

        public string? Name { get; init; }
        public DateTime? LastUpdated => _lastUpdated;

        public double CurrentValue
        {
            get => _currentValue;
            private set => _currentValue = Math.Clamp(value, 0.0, 100.0);
        }

        public CpuUsageMetric(string? name = "CPU Usage")
        {
            Name = name ?? "CPU Usage";
        }

        public async Task UpdateAsync(CancellationToken cancellationToken = default)
        {
            await Task.Delay(100, cancellationToken);

            var simulatedValue = 20.0 + (_random.NextDouble() * 60.0);

            CurrentValue = simulatedValue;
            _lastUpdated = DateTime.UtcNow;
        }
    }

    public sealed class MemoryUsageMetric : IPerformanceMetric<double>
    {
        private readonly Random _random = new();
        private DateTime? _lastUpdated;
        private double _currentValue;

        public string? Name { get; init; }
        public DateTime? LastUpdated => _lastUpdated;
        public double CurrentValue
        {
            get => _currentValue;
            private set => _currentValue = Math.Clamp(value, 0.0, 100.0);
        }

        public MemoryUsageMetric(string? name = "Memory Usage")
        {
            Name = name ?? "Memory Usage";
        }

        public async Task UpdateAsync(CancellationToken cancellationToken = default)
        {
            await Task.Delay(150, cancellationToken);

            var simulatedValue = 40.0 + (_random.NextDouble() * 30.0);

            CurrentValue = simulatedValue;
            _lastUpdated = DateTime.UtcNow;
        }
    }

    // ==================== КЭШ ====================

    public enum CacheRemovalReason
    {
        Expired,
        Removed,
        Replaced,
        Cleanup
    }

    public class CacheItemRemovedEventArgs<TKey> : EventArgs
    {
        public TKey Key { get; }
        public object? Item { get; }
        public CacheRemovalReason Reason { get; }

        public CacheItemRemovedEventArgs(TKey key, object? item, CacheRemovalReason reason)
        {
            Key = key;
            Item = item;
            Reason = reason;
        }
    }

    public class ThreadSafeCache<TKey, TValue> : IDisposable
        where TKey : notnull
        where TValue : class
    {
        private class CacheItem
        {
            public TValue Value { get; }
            public DateTime AddedAt { get; }
            public TimeSpan Expiration { get; }

            public bool IsExpired => DateTime.UtcNow > AddedAt + Expiration;

            public CacheItem(TValue value, TimeSpan expiration)
            {
                Value = value ?? throw new ArgumentNullException(nameof(value));
                AddedAt = DateTime.UtcNow;
                Expiration = expiration;
            }
        }

        private readonly ConcurrentDictionary<TKey, CacheItem> _cache;
        private readonly Timer _cleanupTimer;
        private readonly TimeSpan _cleanupInterval;
        private readonly TimeSpan _defaultExpiration;
        private bool _disposed;

        public event EventHandler<CacheItemRemovedEventArgs<TKey>>? ItemRemoved;

        public ThreadSafeCache(TimeSpan defaultExpiration, TimeSpan cleanupInterval)
        {
            _cache = new ConcurrentDictionary<TKey, CacheItem>();
            _defaultExpiration = defaultExpiration;
            _cleanupInterval = cleanupInterval;
            _cleanupTimer = new Timer(CleanupExpiredItems, null, _cleanupInterval, _cleanupInterval);
        }

        public void AddOrUpdate(TKey key, TValue value, TimeSpan? expiration = null)
        {
            var expirationTime = expiration ?? _defaultExpiration;
            var cacheItem = new CacheItem(value, expirationTime);

            if (_cache.TryGetValue(key, out var oldItem))
            {
                _cache[key] = cacheItem;
                OnItemRemoved(key, oldItem.Value, CacheRemovalReason.Replaced);
            }
            else
            {
                _cache[key] = cacheItem;
            }
        }

        public bool TryGetValue(TKey key, out TValue? value)
        {
            if (_cache.TryGetValue(key, out var cacheItem))
            {
                if (!cacheItem.IsExpired)
                {
                    value = cacheItem.Value;
                    return true;
                }

                RemoveInternal(key, CacheRemovalReason.Expired);
            }

            value = default;
            return false;
        }

        public IEnumerable<TKey> GetKeys()
        {
            return _cache.Keys.ToList();
        }

        public IEnumerable<TValue> GetValues()
        {
            return _cache.Values
                .Where(item => !item.IsExpired)
                .Select(item => item.Value)
                .ToList();
        }

        private void CleanupExpiredItems(object? state)
        {
            try
            {
                var expiredKeys = _cache
                    .Where(kvp => kvp.Value.IsExpired)
                    .Select(kvp => kvp.Key)
                    .ToList();

                foreach (var key in expiredKeys)
                {
                    RemoveInternal(key, CacheRemovalReason.Expired);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Cache cleanup error: {ex.Message}");
            }
        }

        private bool RemoveInternal(TKey key, CacheRemovalReason reason)
        {
            if (_cache.TryRemove(key, out var removedItem))
            {
                OnItemRemoved(key, removedItem.Value, reason);
                return true;
            }

            return false;
        }

        protected virtual void OnItemRemoved(TKey key, object? item, CacheRemovalReason reason)
        {
            ItemRemoved?.Invoke(this, new CacheItemRemovedEventArgs<TKey>(key, item, reason));
        }

        public void Dispose()
        {
            if (!_disposed)
            {
                _cleanupTimer?.Dispose();
                _disposed = true;
            }
        }
    }

    // ==================== СЕРВИС МОНИТОРИНГА ====================

    public class MetricUpdatedEventArgs : EventArgs
    {
        public string MetricId { get; }
        public string MetricName { get; }
        public double Value { get; }
        public DateTime Timestamp { get; }

        public MetricUpdatedEventArgs(string metricId, string metricName, double value)
        {
            MetricId = metricId;
            MetricName = metricName;
            Value = value;
            Timestamp = DateTime.UtcNow;
        }
    }

    public class PerformanceMonitorService : IDisposable
    {
        private readonly ThreadSafeCache<string, IPerformanceMetric<double>> _metricsCache;
        private readonly List<Task> _monitoringTasks;
        private readonly CancellationTokenSource _cts;
        private bool _disposed;

        public event EventHandler<MetricUpdatedEventArgs>? MetricUpdated;

        public PerformanceMonitorService()
        {
            _metricsCache = new ThreadSafeCache<string, IPerformanceMetric<double>>(
                TimeSpan.FromMinutes(5),
                TimeSpan.FromSeconds(30));

            _monitoringTasks = new List<Task>();
            _cts = new CancellationTokenSource();
        }

        public void RegisterMetric(string metricId, IPerformanceMetric<double> metric)
        {
            _metricsCache.AddOrUpdate(metricId, metric);

            var monitoringTask = Task.Run(async () =>
            {
                while (!_cts.Token.IsCancellationRequested)
                {
                    try
                    {
                        await metric.UpdateAsync(_cts.Token);

                        var args = new MetricUpdatedEventArgs(
                            metricId,
                            metric.Name ?? "Unknown",
                            metric.CurrentValue);

                        OnMetricUpdated(args);

                        await Task.Delay(TimeSpan.FromSeconds(2), _cts.Token);
                    }
                    catch (OperationCanceledException)
                    {
                        break;
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error: {ex.Message}");
                        await Task.Delay(TimeSpan.FromSeconds(5), _cts.Token);
                    }
                }
            }, _cts.Token);

            _monitoringTasks.Add(monitoringTask);
        }

        public object GetStatistics()
        {
            var activeMetrics = _metricsCache.GetValues().ToList();

            if (!activeMetrics.Any())
            {
                return new { Message = "No metrics available" };
            }

            return new
            {
                Timestamp = DateTime.Now.ToString("HH:mm:ss"),
                TotalMetrics = activeMetrics.Count,
                AverageValue = activeMetrics.Average(m => m.CurrentValue),
                MaxValue = activeMetrics.Max(m => m.CurrentValue),
                MinValue = activeMetrics.Min(m => m.CurrentValue)
            };
        }

        protected virtual void OnMetricUpdated(MetricUpdatedEventArgs e)
        {
            MetricUpdated?.Invoke(this, e);
        }

        public void Dispose()
        {
            if (!_disposed)
            {
                _cts.Cancel();
                Task.WhenAll(_monitoringTasks).Wait(TimeSpan.FromSeconds(2));
                _cts.Dispose();
                _metricsCache.Dispose();
                _disposed = true;
            }
        }
    }

    // ==================== ОСНОВНАЯ ПРОГРАММА ====================

    public class Program
    {
        public static async Task Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("=================================================");
            Console.WriteLine("     PERFORMANCE MONITORING SYSTEM v2.0");
            Console.WriteLine("=================================================\n");

            using var monitor = new PerformanceMonitorService();

            // Подписываемся на обновления метрик
            monitor.MetricUpdated += (sender, e) =>
            {
                string status = e.Value switch
                {
                    > 80 => "[HIGH]",
                    > 60 => "[MEDIUM]",
                    _ => "[LOW]"
                };

                Console.WriteLine($"[{e.Timestamp:HH:mm:ss}] {status} {e.MetricName,-12}: {e.Value,5:F1}%");
            };

            // Регистрируем метрики
            monitor.RegisterMetric("cpu", new CpuUsageMetric());
            monitor.RegisterMetric("memory", new MemoryUsageMetric());

            Console.WriteLine("Starting 10-second monitoring session...\n");
            Console.WriteLine("---------------------------------------------");
            Console.WriteLine("          LIVE METRICS UPDATES");
            Console.WriteLine("---------------------------------------------");

            // Мониторим 10 секунд
            for (int i = 0; i < 5; i++)
            {
                await Task.Delay(2000);

                var stats = monitor.GetStatistics();
                var statsType = stats.GetType();

                Console.WriteLine($"Iteration {i + 1}:");

                foreach (var prop in statsType.GetProperties())
                {
                    if (prop.Name != "Message")
                    {
                        Console.WriteLine($"  {prop.Name}: {prop.GetValue(stats)}");
                    }
                }

                if (i < 4)
                {
                    Console.WriteLine("---------------------------------------------");
                }
            }

            Console.WriteLine("---------------------------------------------");

            Console.WriteLine("\nMonitoring completed!");
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
