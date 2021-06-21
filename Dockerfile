FROM python:3.9-slim

LABEL maintainer="Boris Ivanov <galacticborey@gmail.com>"

ENV LANG=C.UTF-8 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
