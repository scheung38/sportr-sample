from flask import Flask
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)


def get_url(user_url):
    try:
        r = requests.get(user_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, "html.parser")
        url = soup.findAll(attrs={"property": "og:url"})[0]['content'].encode('utf-8')
        headline = soup.find('title').string
        caption = soup.findAll("figcaption", {"class": "sp-media-asset__caption gel-brevier "})[0].string
        images = soup.findAll(attrs={"property": "og:image"})[0]['content'].encode('utf-8')

        # return json.dumps([{"url": url, "headline": headline, "images": [{"url": images, "caption": caption}]}],
        #                   indent=4, separators=(',', ': '))

        return json.dumps([{"url": url, "headline": headline, "images": [{"url": images, "caption": caption}]}])
    except (requests.exceptions.RequestException, IndexError) as e:
        # print 'Type(e) is :', type(e)
        return e


def start():
    while True:
        s = get_url(raw_input("enter url: "))
        print s, "\n"


if __name__ == '__main__':
    start()
    app.run()
