FROM alpine:3.14

ENV PYTHONUNBUFFERED 1

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g" /etc/apk/repositories

RUN apk add --no-cache \
    python3 \
    py3-pip \
    openssl \
    && mkdir -p /data
    
ADD build/clipboard_server.tar.gz /opt/clipboard_server
    
RUN pip3 install --no-cache-dir tornado \
    && rm -rf /tmp/*

VOLUME ["/data"]

ENV CS_CERT_ADDR=127.0.0.1
ENV CS_DEBUG=false
ENV CS_DATA_DIR=/data
ENV CS_PORT=80
ENV CS_HTTPS_PORT=443
ENV CS_HTTPS_REDIRECT_PORT=443

EXPOSE 80
EXPOSE 443

WORKDIR /opt/clipboard_server

CMD ["/bin/sh", "-c", "./certs/gen_cert.sh && python3 main_server.py"]

