from celery import Celery

celery_app = Celery(
    "image_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "image_tasks.process_images_async": {"queue": "images"},
}
