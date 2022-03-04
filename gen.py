import requests
import json
import os
import string
import random
from random import choice
import binascii
from colorama import *; init()
import uuid
import threading
import multiprocessing

num = 1

def gen():
    global num
    while True:
        with open("proxies.txt", "r") as f:
                proxy1 = choice(f.readlines()).strip()
                proxy = {'https': f'http://{proxy1}'}

        ip = requests.get('https://api.ipify.org', proxies=proxy).text

        x = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))

        username = x
        email = f'{x}@gmail.com'
        password = 'P4ssyboi00'

        headers = {
        'authority': 'www.guilded.gg',
                    'method': 'POST',
                    'path': '/api/users?type=email',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'fr-FR,fr;q=0.9',
                    'content-type': 'application/json',
                    'guilded-client-id': f'{uuid.uuid1()}',
                    'guilded-device-id': str(binascii.b2a_hex(os.urandom(64)).decode('utf-8')),
                    'guilded-device-type': 'desktop',
                    'guilded-stag': 'c4740afd3f3e4d63d365d826139de166',
                    'origin': 'https://www.guilded.gg',
                    'referer': 'https://www.guilded.gg/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                    'dnt': '1',
                    "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
                    "Sec-Ch-Ua-Mobile": '?0',
                    "Sec-Ch-Ua-Platform": "macOS",
        }

        session = requests.Session()

        cookies = session.get('https://www.guilded.gg/', headers = headers, proxies = proxy).cookies

        payload = {"extraInfo":{"platform":"desktop"},"name":username,"email":email,"password":password,"fullName":username}

        response = session.post(f'https://www.guilded.gg/api/users?type=email', json = payload, cookies = cookies, headers = headers, proxies = proxy)

        if response.status_code == 200:
            userID = (json.loads(response.text))['user']['id']
            payload = {"email":email,"password":password,"getMe":True}

            r = session.post('https://www.guilded.gg/api/login', json = payload, cookies = cookies, headers = headers, proxies = proxy)

            payload = {"extraInfo":{"platform":"desktop"},"userId":userID,"teamName":f"{username} server"}

            response = session.post(f'https://www.guilded.gg/api/teams', json = payload, cookies = cookies, headers = headers, proxies = proxy)
            if response.status_code == 200:
                print(f'[{Fore.GREEN}+{Fore.RESET}] Account created -- {email}:{password}:{userID}  |  IP: {Fore.BLUE}{ip}{Fore.RESET}')
                with open('accounts.txt', 'a+')as f:
                    f.write(f'{email}:{password}\n')
            else:
                failedData = json.loads(response.text)
                print(f'[{Fore.RED}-{Fore.RESET}] Account failed --> {Fore.RED}{failedData["message"]}{Fore.RESET}  |  IP: {Fore.BLUE}{ip}{Fore.RESET}')

        else:
            failedData = json.loads(response.text)
            print(f'[{Fore.RED}-{Fore.RESET}] Account failed --> {Fore.RED}{failedData["message"]}{Fore.RESET}  |  IP: {Fore.BLUE}{ip}{Fore.RESET}')

        num = num + 1

if __name__ == '__main__':
    for i in range(1000):
        t1 = multiprocessing.Process(target=gen)
        t1.start()
