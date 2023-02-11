import httpx
import colorama
import time
import requests
import random
from colorama import Fore
colorama.init()

packbible = "https://pastes.io/raw/umas7g2pjv" #You can use your own make sure its a paste raw

w = Fore.WHITE
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX

with open("token.txt") as f:
    tokens = f.readlines()

for token in tokens:
    masked_token = token[:len(token) - 45] + "-"

def tokenchecker():
    tkn2 = token
    headers = {
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Alt-Used": "discord.com",
        "Authorization": tkn2,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "__dcfduid=8ae3ca90b4d911ec998447df76ccab6d; __sdcfduid=8ae3ca91b4d911ec998447df76ccab6d07a29d8ce7d96383bcbf0ff12d2f61052dd1691af72d9101442df895f59aa340; OptanonConsent=isIABGlobal=false&datestamp=Tue+Sep+20+2022+15%3A55%3A24+GMT%2B0200+(hora+de+verano+de+Europa+central)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=ES%3BMD; __stripe_mid=1798dff8-2674-4521-a787-81918eb7db2006dc53; OptanonAlertBoxClosed=2022-04-15T16:00:46.081Z; _ga=GA1.2.313716522.1650038446; _gcl_au=1.1.1755047829.1662931666; _gid=GA1.2.778764533.1663618168; locale=es-ES; __cfruid=fa5768ee3134221f82348c02f7ffe0ae3544848a-1663682124",
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "es-ES",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlcy1FUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDc2MTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    response2 = httpx.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response2.status_code == 200:
            print(f'{w}[{g}+{w}] » Token {g}{masked_token}{w} works')
    if response2.status_code == 204:
            print(f'{w}[{g}+{w}] » Token {g}{masked_token}{w} works')
    if response2.status_code == 403:
        exit()
    if response2.status_code == 404:
        exit()
    if response2.status_code == 401:
        exit()

tokenchecker()

chatpack = requests.get(f'{packbible}')

with open('chatpack.txt', 'w')as file:
    file.write(chatpack.text)


channel_id = input(f'{w}[{g}+{w}] » Channel ID » ')
id_to_pack = input(f'{w}[{g}+{w}] » ID to Pack » ')
delay = input(f'{w}[{g}+{w}] » Delay » ')


url = 'https://discord.com/api/v9/channels/{channel_id}/messages'.format(channel_id=channel_id)
headers = {"authorization": token}

with open("chatpack.txt") as file:
    lines = file.readlines()

letter = f"<@{id_to_pack}> "

start = f"nn <@{id_to_pack}> :rofl:"
data1 = {"content": start}
response = requests.post(url, data=data1, headers=headers)
time.sleep(7)
sentences = random.sample(lines, 300)
for sentence in sentences:
    modified_sentence = letter + sentence
    data = {"content": modified_sentence}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print(f"{w}[{g}+{w}] » Sent Message {sentence}")
    else:
        print(f"{w}[{r}-{w}] » Couldn't send Message {response.status_code}")
    time.sleep(int(delay))
