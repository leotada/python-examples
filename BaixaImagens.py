#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.parse import urljoin
imgs=[]
def main():
    url=str(input('Digite uma URL para pegar as imagens: '))
    if url is '':
        main()
    else:
        html_doc=requests.get(url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        for img in soup.findAll('img'):
                urllib.request.urlretrieve(urljoin(url, img['src']), img['src'].split('/')[-1])
if __name__ == '__main__':
    main()
