from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Docker Flask App работает!",
        "endpoints": [
            "/",
            "/info",
            "/calc/<a>/<b>"
        ]
    })


@app.route("/info")
def info():
    return jsonify({
        "application": "Docker Flask Homework",
        "framework": "Flask",
        "version": "1.0",
        "description": "Учебное Flask-приложение в Docker"
    })


@app.route("/calc/<int:a>/<int:b>")
def calculate(a, b):
    return jsonify({
        "a": a,
        "b": b,
        "result": a + b
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)