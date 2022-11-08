import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

chapterCount = random.randint(1, 21)

url = f'https://biblehub.com/john/{chapterCount}.htm'

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')
chapters = soup.findAll("div", attrs={"class":"chap"})


for verse in chapters:
    pass