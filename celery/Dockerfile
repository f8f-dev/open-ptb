FROM python:3-alpine

RUN addgroup -g 1311 ffgroup
RUN adduser -D -u 1311 -G ffgroup ffuser

WORKDIR /celery

RUN pip install --no-cache-dir celery

COPY . .
