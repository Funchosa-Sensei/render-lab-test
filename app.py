from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
   return "<h1>Версия 2.0</h1><p>Обновил код, сделал git push</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)