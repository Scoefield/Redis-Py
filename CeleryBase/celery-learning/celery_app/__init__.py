from celery import Celery

app = Celery("demo")

app.config_from_object("celery_app.celeryconfig")   # 通过Celery实例加载配置模块
