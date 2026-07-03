#!/usr/bin/env python3
"""
魔法盲盒 — 一键启动服务器
在电脑上双击运行，iPad 扫二维码或输入地址即可打开
"""
import http.server
import socketserver
import socket
import os
import sys
import webbrowser

PORT = 8888
DIR = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

os.chdir(DIR)

# Try to generate QR code in terminal
ip = get_local_ip()
url = f"http://{ip}:{PORT}"

print("""
╔══════════════════════════════════════════╗
║       🎁 魔法盲盒 服务器已启动          ║
║                                          ║
║   📱 在 iPad 的 Safari 中输入：          ║
║                                          ║
║   👉  {url}                    ║
║                                          ║
║   电脑浏览器预览：                        ║
║   👉  http://localhost:8888              ║
║                                          ║
║   按 Ctrl+C 停止服务器                   ║
╚══════════════════════════════════════════╝
""".format(url=url.ljust(42)))

# Try to generate QR code if qrcode module available
try:
    import qrcode
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.print_ascii(invert=True)
    print("\n📷 扫描上方二维码也可打开\n")
except ImportError:
    pass

# Open browser on computer
webbrowser.open(f"http://localhost:{PORT}")

# Start server
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.': 'text/html'})

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n服务器已停止。明天再玩！👋")
