release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn django_project.wsgi:application
worker: celery -A django_project worker -l info
beat: celery -A django_project beat -l info