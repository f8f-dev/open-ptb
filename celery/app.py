from celery import Celery
import os

OPTB_RABBITMQ_CONTAINER_NAME = os.getenv("OPTB_RABBITMQ_CONTAINER_NAME")
OPTB_RABBITMQ_PASSWORD = os.getenv("OPTB_RABBITMQ_PASSWORD")
OPTB_RABBITMQ_PORT = os.getenv("OPTB_RABBITMQ_PORT")
OPTB_RABBITMQ_USER = os.getenv("OPTB_RABBITMQ_USER")
BROKER_URL = f"amqp://{OPTB_RABBITMQ_USER}:{OPTB_RABBITMQ_PASSWORD}@{OPTB_RABBITMQ_CONTAINER_NAME}:{OPTB_RABBITMQ_PORT}//"

worker = Celery(
    "my_bot",
    broker=BROKER_URL,
    # backend=BROKER_URL,  # для простоты можно использовать тот же брокер
)
