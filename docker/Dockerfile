FROM alpine:3.14

ENV PYTHONUNBUFFERED 1

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g" /etc/apk/repositories

RUN apk add --no-cache \
    python3 \
    py3-pip \
    && mkdir -p /data
    
ADD clipboard_server.tar.gz /opt/clipboard_server
    
RUN pip3 install --no-cache-dir tornado \
    && rm -rf /tmp/*

VOLUME ["/data"]

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["/opt/clipboard_server/main_server.py"]