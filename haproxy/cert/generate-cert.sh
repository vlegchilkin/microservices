#!/bin/sh

cd "$(dirname "$0")"

SUBJECT='/CN=localhost/subjectAltName=DNS:test,DNS:test.local'

if [ ! -s "cert.pem" ] ; then
  echo "Generating key and self-signed certificate for $SUBJECT"
  openssl req -subj "$SUBJECT" -x509 -newkey rsa:2048 -nodes -keyout "key.pem" -out "cert.pem" -days 3650
fi

cat key.pem cert.pem > haproxy.pem
