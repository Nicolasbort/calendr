FROM python:3.11.2-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev\
    libffi-dev openssl-dev cargo

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /usr/src/app/logs
RUN touch /usr/src/app/logs/application.logs

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]