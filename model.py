from celery import Celery
from time import sleep

app = Celery("tasks", backend="redis://localhost:6379",
             broker="redis://localhost:6379")

@app.task
def process_image(image=None):
    print(image)
    sleep(10)
    return {"res": [1, 2, 3, image]}
