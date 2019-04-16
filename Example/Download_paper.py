import sys
import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Host': 'sci-hub.tw',
    'Referer': 'http://sci-hub.tw/',
    'Upgrade-Insecure-Requests': '1'
}
def Download_pdf(doi,name):
    url = 'http://sci-hub.tw/'+doi
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")
    URL = soup.iframe['src']
    path=name
    r=requests.get(URL)
    print("ok")
    with open(path,"wb") as f:
        f.write(r.content)
    f.close()

doi = sys.argv[1]
name = sys.argv[2]
Download_pdf(doi,name)
