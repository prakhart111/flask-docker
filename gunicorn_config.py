# inbuilt packages
import os
import multiprocessing 

workers = multiprocessing.cpu_count() * 2 + 1
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
worker_class = 'gevent'
worker_connections = 1000
forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }