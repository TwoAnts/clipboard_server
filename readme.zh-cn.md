# Clipboard-Server

纯Web实现。

使用WebSocket实现彼此通信。

## 使用场景

当你想跨设备拷贝一些文本时，可以在两端同时打开浏览器，并打开此页面。

粘贴并发送内容，就这么简单。

## docker compose

```
version: "3.8"
services:
  cilpboard:
    image: rainbowhu/clipboard_server:latest
    ports:
      - "${CB_HTTP_PORT}:80"
      - "${CB_HTTPS_PORT}:443"
    environment:
      - CS_PORT=80
      - CS_HTTPS_PORT=443
      - CS_CERT_ADDR=${HOST_IP} # 外部访问IP
      - CS_HTTPS_REDIRECT_PORT=${CB_HTTPS_PORT} # 外部访问端口号
    network_mode: "bridge"
    restart: unless-stopped
```

## 待实现

- [x] 网页URL通过二维码呈现
- [x] 打包docker镜像
- [ ] 增加实现截图
