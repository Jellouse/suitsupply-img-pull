import requests
from bs4 import BeautifulSoup
import wget
import os
import re
import sys


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# define current working direcory
cwd = os.getcwd()
out = cwd + "/output"


url = str(sys.argv[1])

page = requests.get(url, headers)
soup = BeautifulSoup(page.content, 'html.parser')
pdpImageClass = soup.find(class_='pdp-images js-pdp-images')
pdpImages = pdpImageClass.find_all("img")

tag = pdpImages[0]

for i in range(len(pdpImages)):
    imgUrl = pdpImages[i]['data-src']

    imgUrl = re.split('(/)', imgUrl)

    del imgUrl[9:13]
    imgUrl = ''.join(imgUrl)
    imgUrl = imgUrl.replace('.jpg', '.png')

    imgFile = wget.download(imgUrl, out = out)

