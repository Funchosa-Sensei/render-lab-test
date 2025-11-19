from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Лабораторная работа выполнена!</h1><p>Приложение работает на Render (аналог Heroku).</p>"

if __name__ == '__main__':
    # Получаем порт, который выдаст облако, или используем 5000 по умолчанию
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)