# gunicorn.conf.py
import os

workers = int(os.getenv('GUNICORN_WORKERS', '4'))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2
errorlog = '-'
loglevel = 'info'
accesslog = '-'