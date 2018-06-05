FROM alpine:latest

RUN apk update && \
    apk add bash python3 python3-dev py3-pip supervisor build-base linux-headers && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install uwsgi django

EXPOSE 8000
COPY app /app/
COPY config /etc/app/
WORKDIR /app/
CMD ["supervisord", "-n", "-c", "/etc/app/supervisor.conf"]
