# Docker Flask Homework

Учебное Flask-приложение, контейнеризированное с помощью Docker.

Проект выполнен в рамках урока **«Docker для вайбкодера»**.

## Возможности

Приложение содержит 3 HTTP-эндпоинта:

* `GET /` — главная страница и список доступных эндпоинтов;
* `GET /info` — информация о приложении;
* `GET /calc/<a>/<b>` — сложение двух чисел.

## Технологии

* Python 3.12
* Flask 3.0.3
* Docker
* Docker Compose

## Структура проекта

```text
docker-flask-homework/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Запуск через Docker

Собрать Docker-образ:

```bash
docker build -t my-flask-app .
```

Запустить контейнер:

```bash
docker run -d -p 5000:5000 my-flask-app
```

После запуска приложение доступно по адресу:

```text
http://localhost:5000
```

## Запуск через Docker Compose

Запустить приложение:

```bash
docker compose up -d
```

Проверить запущенные контейнеры:

```bash
docker ps
```

Остановить приложение:

```bash
docker compose down
```

## API

### Главная страница

```text
GET /
```

Пример:

```text
http://localhost:5000/
```

Ответ:

```json
{
  "message": "Docker Flask App работает!",
  "endpoints": [
    "/",
    "/info",
    "/calc/<a>/<b>"
  ]
}
```

### Информация о приложении

```text
GET /info
```

Пример:

```text
http://localhost:5000/info
```

Ответ:

```json
{
  "application": "Docker Flask Homework",
  "description": "Учебное Flask-приложение в Docker",
  "framework": "Flask",
  "version": "1.0"
}
```

### Калькулятор

```text
GET /calc/<a>/<b>
```

Пример:

```text
http://localhost:5000/calc/10/25
```

Ответ:

```json
{
  "a": 10,
  "b": 25,
  "result": 35
}
```

## Docker

Для приложения используется Dockerfile на основе `python:3.12-slim`.

Docker Compose автоматически:

1. собирает Docker-образ;
2. создаёт контейнер;
3. пробрасывает порт `5000`;
4. запускает Flask-приложение.

## Автор

Учебный проект по курсу **«Профессия вайб-кодер»**.
