FROM python:alpine

RUN apk add --update --no-cache gcc postgresql-dev python3-dev musl-dev && \
    pip3 install uwsgi flask peewee psycopg2 && \
    rm -r /root/.cache && \
    apk del gcc

EXPOSE 8000
COPY config /etc/uwsgi
WORKDIR /app/web/

CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
