# syntax=docker/dockerfile:1

FROM python:3.10.12-slim AS image

LABEL maintainer="Tigran Saatchyan <mr.saatchyan@yandex.com>"
LABEL description="This is a custom Docker image for AtomicProgress application."
LABEL version="1.0"
LABEL release-date="2023-10-14"
LABEL org.opencontainers.image.title="AtomicProgress App"
LABEL org.opencontainers.image.description="AtomicProgress application in a Docker container"
LABEL org.opencontainers.image.version="1.0"
LABEL org.opencontainers.image.created="2023-10-14"

FROM image AS build-stage

ARG POETRY_VERSION=1.6.0
ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=60 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}
RUN apt-get install -y build-essential libpq-dev && apt-get clean
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

FROM build-stage AS requirements

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

COPY ./poetry.lock ./pyproject.toml ${APP_HOME}/
RUN poetry install --no-root

FROM requirements AS install-app

COPY --chown=appuser:appuser /app ${APP_HOME}
RUN chown -R appuser:appuser ${APP_HOME}

COPY --chown=appuser:appuser ./docker/migrate.sh /migrate
COPY --chown=appuser:appuser ./docker/start.sh /start
COPY --chown=appuser:appuser ./docker/start_celery_worker.sh /start-celery-worker
COPY --chown=appuser:appuser ./docker/start_celery_beat.sh /start-celery-beat

RUN sed -i 's/\r$//g' /migrate
RUN sed -i 's/\r$//g' /start
RUN sed -i 's/\r$//g' /start-celery-worker
RUN sed -i 's/\r$//g' /start-celery-beat

RUN chmod u+x /migrate
RUN chmod u+x /start
RUN chmod u+x /start-celery-worker
RUN chmod u+x /start-celery-beat

USER appuser

EXPOSE 8000
