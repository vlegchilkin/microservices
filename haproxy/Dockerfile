FROM haproxy:2.9-alpine

USER root

ENV TZ=${TZ:-Europe/Berlin}

RUN apk add --no-cache tzdata

COPY cert /usr/local/etc/haproxy/cert
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
