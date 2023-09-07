#!/bin/sh -x

BASE_DIR="$(cd "$(dirname "$0")"; pwd)";

openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 36500 \
            -nodes \
            -out "$BASE_DIR"/cs.crt \
            -keyout "$BASE_DIR"/cs.key \
            -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=HZY/OU=IT Department/CN=$CS_CERT_ADDR"

