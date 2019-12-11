from python:3.8.0-alpine

run apk update && apk --update add bash

workdir /app
copy poetry.lock ./
copy pyproject.toml ./
run pip install poetry && poetry install

copy ./* ./

run ln -s /app/.aws ~/.aws
