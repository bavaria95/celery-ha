188.184.94.146:
- 5672 RabbitMQ
- 7000 Redis

188.184.89.215:
- 5000 gunicorn (`gunicorn app:app -b 0.0.0.0:5000 -w 1 --log-level debug -t 600`)
- celery (`celery -A tasks worker --loglevel=info`)

