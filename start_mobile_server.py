#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
西藏自驾保障系统 - iOS / 移动设备局域网实时传输与车机投屏服务
自动识别 Mac Wi-Fi IP，生成终端可扫描二维码，并启动高性能本地服务供 iPhone/iPad 即刻连接
"""

import os
import sys
import subprocess
import socket
import http.server
import socketserver
import qrcode

PORT = 8000

def get_mac_wifi_ip():
    """获取 Mac 在当前 Wi-Fi/热点局域网中的真实 IP"""
    for iface in ['en0', 'en1']:
        try:
            res = subprocess.check_output(['ipconfig', 'getifaddr', iface], stderr=subprocess.DEVNULL).decode('utf-8').strip()
            if res:
                return res
        except Exception:
            pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

def print_banner(ip):
    app_url = f"http://{ip}:{PORT}/weather_road_app.html"
    hub_url = f"http://{ip}:{PORT}/index.html"
    
    print("\n" + "=" * 64)
    print("🏔️  西藏自驾 48 行政区实时气象与重大地灾通报系统 - iOS 传输中心")
    print("=" * 64)
    print(f"\n📡 当前局域网服务器已就绪！")
    print(f"👉 iPhone 访问地址： {app_url}")
    print(f"👉 46天全景路书地址： {hub_url}\n")
    print("📱 请用 iPhone 自带【相机】直接对准下方二维码扫描打开：\n")
    
    qr = qrcode.QRCode(border=2)
    qr.add_data(app_url)
    qr.print_ascii(invert=True)
    
    print("\n" + "-" * 64)
    print("📲【iPhone 最佳实践·安装为独立 App 指南】")
    print("  1. 在 iPhone Safari 浏览器中打开上方网址；")
    print("  2. 点击 Safari 底部中央的「分享」按钮（带有向上箭头的方框）；")
    print("  3. 向上滑动菜单，点击【添加到主屏幕】（Add to Home Screen）；")
    print("  4. 此时 iPhone 桌面上将生成独立「西藏自驾通报」原生 App 图标！")
    print("  5. 点击图标全屏无地址栏沉浸式运行，行车中连接车载蓝牙/CarPlay，")
    print("     特级地灾警报与天气将直接通过汽车原装音响高保真播报！")
    print("-" * 64 + "\n")
    print("💡 按 Ctrl+C 可停止当前局域网服务。\n")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run():
    ip = get_mac_wifi_ip()
    print_banner(ip)
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = http.server.SimpleHTTPRequestHandler
    with ReusableTCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 局域网服务已安全停止。")

if __name__ == '__main__':
    run()
