FROM python:3.10.12-slim AS image

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       python3-dev \
       libpq-dev \
       && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY /app/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
