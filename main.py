
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!\n tselthskdfjgdlgjdlkfg\n jgdfngljkdsfnhksrjlthystjlghlkfgh\n"

@app.route('/healthy')
def healthy():
    # Возвращает JSON-ответ с сообщением и статусом 200
    return jsonify(status="healthy", message="Server is healthy!"), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
