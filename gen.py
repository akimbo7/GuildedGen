import requests
import json
import os
import string
import random
from random import choice
import binascii
from colorama import *; init()
import uuid
from concurrent.futures import ThreadPoolExecutor
import datetime

successAccounts = 0
failedAccounts = 0

def gen():
    global successAccounts
    global failedAccounts
    try:
        while True:
            with open("proxies.txt", "r") as f:
                    proxy1 = choice(f.readlines()).strip()
                    proxy = {'https': f'http://{proxy1}'}

            x = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))

            username = x
            email = f'{x}@gmail.com'
            password = 'iLoveAkimbo7'

            headers = {
                        'authority': 'www.guilded.gg',
                        'method': 'POST',
                        'path': '/api/users?type=email',
                        'scheme': 'https',
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
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

            session.headers.update(headers)
            session.proxies.update(proxy)
            session.get('https://www.guilded.gg/')

            payload = {"extraInfo":{"platform":"desktop"},"name":username,"email":email,"password":password,"fullName":username}

            response = session.post(f'https://www.guilded.gg/api/users?type=email', json = payload)
            hmacCookie = response.cookies['hmac_signed_session']

            if response.status_code == 200:
                userID = (json.loads(response.text))['user']['id']
                payload = {"email":email,"password":password,"getMe":True}

                r = session.post('https://www.guilded.gg/api/login', json = payload)

                payload = {"extraInfo":{"platform":"desktop"},"userId":userID,"teamName":f"{username} server"}

                response = session.post(f'https://www.guilded.gg/api/teams', json = payload)
                if response.status_code == 200:

                    x = datetime.datetime.now()
                    successAccounts += 1
                    print(f'[{Fore.MAGENTA}{x.strftime("%H:%M:%S.%f")[:-4]}{Fore.RESET}] (Account No.{successAccounts}) [{Fore.GREEN}+{Fore.RESET}] Account created -- {email} : {password} : {hmacCookie[:20]}.....{hmacCookie[-20:]}')
                    with open('accounts.txt', 'a+')as f:
                        f.write(f'{email}:{password}:{hmacCookie}\n')
                else:
                    x = datetime.datetime.now()
                    failedAccounts += 1
                    failedData = json.loads(response.text)
                    print(f'[{Fore.MAGENTA}{x.strftime("%H:%M:%S.%f")[:-4]}{Fore.RESET}] [{Fore.RED}-{Fore.RESET}] Account failed --> {Fore.RED}{failedData["message"]}{Fore.RESET}')

            else:
                x = datetime.datetime.now()
                failedAccounts += 1
                failedData = json.loads(response.text)
                print(f'[{Fore.MAGENTA}{x.strftime("%H:%M:%S.%f")[:-4]}{Fore.RESET}] [{Fore.RED}-{Fore.RESET}] Account failed --> {Fore.RED}{failedData["message"]}{Fore.RESET}')

    except Exception as e:
        x = datetime.datetime.now()
        print(f'[{Fore.MAGENTA}{x.strftime("%H:%M:%S.%f")[:-4]}{Fore.RESET}] [{Fore.RED}-{Fore.RESET}] Error --> {Fore.RED}{e}{Fore.RESET}')

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=100) as ex :
        for x in range(100):
            ex.submit(gen)
