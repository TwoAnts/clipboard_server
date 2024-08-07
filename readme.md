# Clipboard-Server

[中文说明](readme.zh-cn.md)

Pure Web Implement.

Use WebSocket to sync with each other.

## Use Case 

When you want to copy some text crossing devices, you can use browser and open the page.

Paste and send content, very simple.

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
      - CS_CERT_ADDR=${HOST_IP}
      - CS_HTTPS_REDIRECT_PORT=${CB_HTTPS_PORT}
    network_mode: "bridge"
    restart: unless-stopped
```

## Todo

- [x] Provide QR Code for the page URL
- [x] Build docker image
- [ ] Add preview in readme
