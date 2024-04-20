ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip uv && \
    uv pip install --system -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . .

ENV DJANGO_ALLOWED_HOSTS "place-holder"
ENV DJANGO_CSRF_TRUSTED_ORIGINS "place-holder"
ENV DJANGO_DEFAULT_FROM_EMAIL "place-holder"
ENV DJANGO_SERVER_EMAIL "place-holder"
ENV DJANGO_EMAIL_HOST "place-holder"
ENV DJANGO_EMAIL_PORT "place-holder"
ENV DJANGO_EMAIL_HOST_USER "place-holder"
ENV DJANGO_EMAIL_HOST_PASSWORD "place-holder"
ENV DATABASE_URL "place-holder"
ENV REDIS_URL "place-holder"

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]
