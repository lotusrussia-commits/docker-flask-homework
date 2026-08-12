from flask import Flask, jsonify
import requests
import time
import json

app = Flask(__name__)

LOKI_URL = "http://host.docker.internal:3100/loki/api/v1/push"


def send_log_to_loki(message, app_name="my_app", level="INFO"):
    timestamp = str(time.time_ns())

    payload = {
        "streams": [
            {
                "stream": {
                    "app": app_name,
                    "level": level
                },
                "values": [
                    [timestamp, message]
                ]
            }
        ]
    }

    try:
        response = requests.post(
            LOKI_URL,
            json=payload,
            timeout=5
        )

        if response.status_code == 204:
            print(f"✓ [{level}] {message}")
        else:
            print(
                f"✗ Ошибка отправки в Loki: "
                f"{response.status_code} {response.text}"
            )

    except Exception as e:
        print(f"✗ Ошибка подключения к Loki: {e}")


@app.route("/")
def home():
    send_log_to_loki(
        "Был запрошен главный экран",
        "my_app",
        "INFO"
    )

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
    send_log_to_loki(
        "Запрошена информация о приложении",
        "my_app",
        "INFO"
    )

    return jsonify({
        "application": "Docker Flask Homework",
        "framework": "Flask",
        "version": "1.0",
        "description": "Учебное Flask-приложение в Docker"
    })


@app.route("/calc/<int:a>/<int:b>")
def calculate(a, b):
    result = a + b

    send_log_to_loki(
        f"Выполнен расчёт: {a} + {b} = {result}",
        "my_app",
        "SUCCESS"
    )

    return jsonify({
        "a": a,
        "b": b,
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)