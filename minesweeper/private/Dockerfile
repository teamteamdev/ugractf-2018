FROM python:alpine

RUN apk add --update --no-cache gcc postgresql-dev python3-dev musl-dev && \
    pip3 install -r flask peewee psycopg2 && \
    rm -r /root/.cache && \
    apk del build-base linux-headers postgresql-dev

EXPOSE 8000
COPY config /etc/uwsgi
WORKDIR /app/web/

CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
