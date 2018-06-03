FROM python:3-alpine

RUN apk add --update --no-cache gcc python3-dev socat && \
    pip3 install flask peewee && \
    rm -r /root/.cache && \
    apk del gcc

WORKDIR /app
COPY server /app
RUN chmod +x /app/server.py && python3 /app/init.py && mkdir /tmp/gameserver/
CMD ["socat", "-T", "5", "tcp-l:31337,pktinfo,reuseaddr,fork", "exec:/app/server.py"]
EXPOSE 31337