#!/bin/sh -x

rm -rf build
mkdir -p build

tar -C .. --exclude-vcs --exclude=docker -cf build/clipboard_server.tar .
gzip build/clipboard_server.tar

#docker build
docker build -t clipboard_server:v1.1 .

