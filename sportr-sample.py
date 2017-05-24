from flask import Flask
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def method_name(user_url):
    r = requests.get(user_url)
    # print 'r.headers is : ', r.headers['content-type']
    # print 'r.encoding is : ', r.encoding
    # print 'r.text is : ', r.text
    soup = BeautifulSoup(r.text, "html.parser")
    # print 'type(soup) is : ', type(soup), "\n"  # <class 'bs4.BeautifulSoup'>
    url = soup.findAll(attrs={"property": "og:url"})[0]['content'].encode('utf-8')
    # print 'url is :', url, "\n"
    headline = soup.find('title').string
    # print 'headline is : ', headline, "\n"
    caption = soup.findAll("figcaption", {"class": "sp-media-asset__caption gel-brevier "})[0].string
    # print 'caption is : ', caption, "\n"
    images = soup.findAll(attrs={"property": "og:image"})[0]['content'].encode('utf-8')
    # print 'images is : ', images, "\n"
    # print 'soup.prettify is : ', soup.prettify(), "\n"

    return json.dumps([{"url": url, "headline": headline, "images": [{"url": images, "caption": caption}]}],
                      indent=4, separators=(',', ': '))


# test1 = method_name('http://www.bbc.co.uk/sport/tennis/37268846')
# test2 = method_name('http://www.bbc.co.uk/sport/formula1/40033528')
# test3 = method_name('http://www.bbc.co.uk/sport/football/40031876')

# print test1, "\n"
# print test2, "\n"
# print test3, "\n"


def input_complete(input_list):
    if ";" in input_list[-1]:
        return True
    else:
        return False


def get_input(prompt1, prompt2):
    L = list()
    prompt = prompt1
    while True:
        L.append(raw_input(prompt))
        if input_complete(L):
            return method_name(prompt1)
            # return "\n".join(L)
        prompt = prompt2


if __name__ == '__main__':
    # s = get_input("enter url: ", "? ")
    # s = raw_input("enter url: ")
    test = method_name('http://www.bbc.co.uk/sport/tennis/37268846')
    print test
    # method_name(s)
    # print repr(s)
    app.run()
