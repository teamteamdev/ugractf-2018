FROM python:3-alpine

RUN apk add --update --no-cache gcc postgresql-dev python3-dev musl-dev socat && \
    pip3 install -r flask peewee && \
    rm -r /root/.cache && \
    apk del build-base linux-headers postgresql-dev

COPY server /app
CMD ["socat", "-T", "5", "tcp-l:31337,pktinfo,reuseaddr,fork", "exec:/app/server.py"]
EXPOSE 1234
