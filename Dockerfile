FROM python:3.6-alpine

RUN apk add --no-cache bash postgresql postgresql-client postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev git jpeg-dev zlib-dev alpine-sdk

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

EXPOSE 8000

ADD ./docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]
