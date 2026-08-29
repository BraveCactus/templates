import os
from flask import Flask

app = Flask(__name__)

# Переменные окружения со значениями по умолчанию
GREETING = os.getenv('GREETING', 'Hello')
PORT = int(os.getenv('PORT', 5000))
DATA_DIR = os.getenv('DATA_DIR', '/data')   # папка для монтирования
COUNTER_FILE = os.path.join(DATA_DIR, 'counter.txt')

def read_counter():
    """Читает текущее значение счётчика из файла."""
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def write_counter(value):
    """Записывает новое значение счётчика в файл."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(value))

@app.route('/')
def index():
    counter = read_counter() + 1
    write_counter(counter)
    return f"{GREETING}, world! You are visitor #{counter}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)