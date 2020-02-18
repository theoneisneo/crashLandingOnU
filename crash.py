import os

from bs4 import BeautifulSoup
import requests

for i in range(1, 8):
    url1 = f"http://program.tving.com/tvn/cloy/5/Board/List?page={i}"
    r1 = requests.get(url1)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    a_tags = soup1.find_all('a')
    for a in a_tags:
        link1 = a.get('href')
        if link1.startswith('/tvn/cloy/5/Board/View?'):
            url2 = f"http://program.tving.com/{link1}"
            r2 = requests.get(url2)
            soup2 = BeautifulSoup(r2.text, 'html.parser')
            img_tags = soup2.find_all('img')
            for b in img_tags:
                link2 = b.get('src')
                if link2.endswith('.png') or link2.endswith('.jpg'):
                    os.system(f"wget {link2}")