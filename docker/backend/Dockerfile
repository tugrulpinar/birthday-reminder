FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip uv

RUN set -ex && \
    uv pip install --system -r requirements.txt && \
    rm -rf /root/.cache/

COPY . .
