
import os
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
xanh = "\033[1;36m"
thanh = f'{trang}=> [⚡]'     
        
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"

# import lại
import string
import requests
import random
from collections import defaultdict    
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box
from colorama import init
import cloudscraper
from colorama import Fore, init
from pystyle import Colors, Colorate 

import requests
import random
import string
import hashlib,os
scraper = cloudscraper.create_scraper()
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
hongnhat = "#FFC0CB"
kt_code = "🌸"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;39m[\033[1;32m ¤ \033[1;39m] \033[32;5;245m\033[1m\033[38;5;39m=> "

import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import Fore, init
from colorama import init
from pystyle import Colors, Colorate 
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"


colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương 
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

def thanhngang(so):
    for i in range(so):
        print(range+'\033[1;31m-',end ='')
    print('')

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

kiem_tra_mang()

def banner():
    import os
    from pystyle import Colors, Colorate

    logo = r"""
██╗░░░██╗██╗███╗░░██╗██╗░░██╗
██║░░░██║██║████╗░██║██║░░██║
╚██╗░██╔╝██║██╔██╗██║███████║
░╚████╔╝░██║██║╚████║██╔══██║
░░╚██╔╝░░██║██║░╚███║██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""

    info = f"""
\033[1;36m╭──────────────────────────────────────────────────────╮
\033[1;97m│ 👤 Admin     : \033[1;96mVõ Thanh Vinh
\033[1;97m│ 📺 YouTube   : \033[1;96mhttps://youtube.com/@vothanhvinh88
\033[1;97m│ 💬 Zalo Box  : \033[1;96mhttps://zalo.me/g/mnrjbv086
\033[1;97m│ 💠 Telegram  : \033[1;96mhttps://t.me/vinhdvfb
\033[1;97m│ 🔔 Thông Báo : \033[1;96mMua key Vip chỉ với 20k/1tháng 🔹
\033[1;36m╰──────────────────────────────────────────────────────╯
"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Diagonal(Colors.blue_to_white, logo, 1))
    print(info)
    print(Colorate.Diagonal(Colors.white_to_green, "╰────────────────────────────────────────────────────────────────────╯"))

os.system('cls' if os.name== 'nt' else 'clear')
banner()
sleep(1.2)

    # Nhập auth golike
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input(f"{trang}>> {luc}Nhập Authorization Golike : {trang}")
  token = input(f"{trang}>> {luc}Nhập T (Token): {trang}")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  print(f"{trang}>> {luc}Nhập {trang}[{vang}1{trang}] {luc}Để Vào Tool Pinterest")
  print(f"{trang}>> {luc}Nhập {trang}[{vang}2{trang}] {luc}Để Xóa Authorization Hiện Tại")
  print(f"{trang}──────────────────────────────────────────────────────────────────────")
  
  select = input(f"{trang}>> {luc}Nhập Lựa Chọn :{trang} ")
  kiem_tra_mang()
  if select != "1":
    author = select
  if select == "2":
    for i in range(1, 101):
     sys.stdout.write(f"\r{BOLD}{AQUA} ĐANG TIẾN HÀNH XÓA AUTH CŨ : [{i}% {'║' * (i // 2)}]{RESET}")
     sys.stdout.flush()
     sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
    os.system('cls' if os.name== 'nt' else 'clear')
    print(banner)
    author = input(f"{trang}>> {luc}Nhập Auth Golike Mới : {trang}")
    token = input(f"{trang}>> {luc}Nhập T Golike Mới : {trang}")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
os.system('cls' if os.name== 'nt' else 'clear')
banner()
print(f"{trang}>> {luc}Danh Sách Acc Pinterest :")
print(f"{trang}──────────────────────────────────────────────────────────────────────")
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/pinterest',
}

scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    try:
      response = scraper.get(
        'https://gateway.golike.net/api/pinterest-account',
    
        headers=headers,
        json=json_data
     ).json()
      return response
    except Exception:
      sys.exit()

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
   
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/pinterest/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception:
      sys.exit()

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/pinterest/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception:
      sys.exit()

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }

        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }

        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/pinterest/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception:
      sys.exit()

# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontktiktok = chonacc()

def dsacc():
  if chontktiktok.get("status") != 200:  
    print("{do}Authorization Hoăc T Sai ")
    quit()
  for i in range(len(chontktiktok["data"])):
    print(f"{trang}[{vang}{i+1}{trang}] >> {xanh}Name {trang}: {tim}{chontktiktok["data"][i]["name"]} {trang}| {luc}Hoạt Động")
dsacc() 
print(f"{trang}──────────────────────────────────────────────────────────────────────")
while True:
  try:
    luachon = int(input(f"{trang}>> {luc}Chọn tài khoản:{trang} "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input(f"{trang}>> {luc}Acc Không Tồn Tại,Vui Lòng Nhập Lại : {trang}"))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print(f"{do}Sai Định Dạng ") 
while True:
  try:
    os.system('cls' if os.name== 'nt' else 'clear')
    banner()
    delay = int(input(f"{trang}>> {luc}Delay Thực Hiện job : {trang}"))
    break
  except:
    print("{do}Sai Định Dạng ")
# Nhập proxy
proxy_input = input(f"{trang}>> {luc}Nhập proxy (host:port hoặc user:pass@host:port), Enter nếu không dùng đến : {trang}").strip()
proxies = {
    "http": f"http://{proxy_input}",
    "https": f"http://{proxy_input}"
} if proxy_input else None
    
os.system('cls' if os.name== 'nt' else 'clear')
banner()
print(f"{trang}>> {luc}Nhập {trang}[{vang}1{trang}] {luc}Để Làm Job Follow ")

while True:
    try:
        loai_nhiem_vu = int(input(f"{trang}>> {luc}Chọn Nhiệm Vụ: {trang}"))
        if loai_nhiem_vu in [1]:
            break
        else:
            print(f"{do}Vui Lòng Chọn Số Từ 1")
    except:
        print(f"{do}Sai Định Dạng! Vui Lòng Nhập Số.")  
  
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ
   
dem = 0
tong = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

banner()
print("")
while True:
    
    print(f"{tim}Đang Get Job  ", end="\r")
    max_retries = 3
    retry_count = 0
    nhanjob = None

    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception as e:
            retry_count += 1
            time.sleep(1)

    if not nhanjob or retry_count >= max_retries:
        continue

    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]
# Kiểm tra loại nhiệm vụ
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue
    # Đếm ngược delay
    for remaining_time in range(delay, -1, -1):
        color = "\033[1;35m" if remaining_time % 2 == 0 else "\033[1;36m"
        print(f"\r{color} Thtool Auto Kiếm Tiền [{remaining_time}s]   ", end="")
        time.sleep(1)
    print("\r                          \r", end="") 
    color = "\033[1;35m" if remaining_time % 2 == 0 else "\033[1;33m"
    print(f"{color} Đang Nhận Tiền Lần 1 ... ",end = "\r")
    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        thoigian = time.strftime("%H:%M:%S", time.localtime())
        console = Console()                             
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("STT", style="bold yellow")
        table.add_column("Thời gian", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Tiền ", style="bold green")
        table.add_column("Tổng Tiền", style="bold white")
        table.add_row(
        str(dem),
        thoigian,
        "[green]SUCCESS[/green]",
        f"[bold green]+{tien}đ",
        f"[bold yellow]{tong} vnđ"
    )

        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        console.print(table)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print(f"{do}Bỏ Qua Job Lỗi Thành Công ", end="\r")
            sleep(1.5)
            checkdoiacc += 1
        except:
            pass



