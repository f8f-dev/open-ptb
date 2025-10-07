В боте исполуется Celery чтобы поочередно обрабатывать сообщения от пользователя.

TODO:
move to fluentd bit?
### How to run?
1. Create docker network.
```sh
docker network create internal_bridge
```
2. Create docker volume.
```sh
docker volume create celery_logs
docker volume create rabbitmq_data
docker volume create rabbitmq_logs
```