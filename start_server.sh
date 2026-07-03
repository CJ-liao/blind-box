#!/bin/bash
# 魔法盲盒 — 本地服务器启动脚本
# 在同一 WiFi 下，iPad 用 Safari 打开 http://你的电脑IP:8888

PORT=8888
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "========================================"
echo "  🎁 魔法盲盒 — 本地服务器"
echo "========================================"
echo ""
echo "  在 iPad 上打开 Safari，输入地址："
echo ""

# Get local IP
IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)
if [ -n "$IP" ]; then
    echo "  👉 http://$IP:$PORT"
    echo ""
else
    echo "  👉 http://localhost:$PORT"
    echo ""
fi

echo "  按 Ctrl+C 停止服务器"
echo "========================================"
echo ""

cd "$DIR"
python3 -m http.server $PORT --bind 0.0.0.0 2>/dev/null || python3 -m http.server $PORT
