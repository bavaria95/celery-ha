# celery-ha
[slides](http://slides.com/dimapetruk/ha-celery#/)

Files for the invenio-dev forum presentation about high available Celery.

Shows tasks and app that generates stream of tasks, waits until the last one is finished and measures taken time.

Tests two different setups:
* basic one with one RabbitMQ as message broker and one Redis as result backend
* with clustered RabbitMQ as message broker and master/slave Redis as result backend

