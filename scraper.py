#!/usr/bin/env python3.4
# Scrapes the HTML edition of GG from the Internet
import os
import requests

from bs4 import BeautifulSoup

GG_URL = 'https://www.gesetze-im-internet.de/gg/BJNR000010949.html'
GG_FILE_NAME = 'gg.txt'


def download_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None


def strip_links_to_toc(html):
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all(True):
        if tag.name in ['a']:
            tag.replaceWith('')
    return soup.find(id='container').text


def save_to_disk(text):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, GG_FILE_NAME)
    with open(file_path, 'w') as fh:
        fh.write(text)
    print('Downloaded GG text from ' + GG_URL + ' to disk as ' + GG_FILE_NAME)

if __name__ == '__main__':
    html = download_html(GG_URL)
    text = strip_links_to_toc(html)
    save_to_disk(text)
