FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./conf/requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /app

ARG APP_ID=1000

RUN groupadd -g "$APP_ID" app \
  && useradd -g "$APP_ID" -u "$APP_ID" -d /app -s /bin/bash app

USER app:app