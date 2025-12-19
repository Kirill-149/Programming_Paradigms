# features/environment.py
import sys
import os

# Добавляем путь к пакету в начало sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

print(f"Python path: {sys.path}")
print(f"Current directory: {os.getcwd()}")
