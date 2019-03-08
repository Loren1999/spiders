import requests
from lxml import etree
from fake_useragent import UserAgent
import json
import time
import threading


def get_random_ua():  # 随机UA
    ua = UserAgent()
    return ua.random


headers = {
    'User-Agent': get_random_ua()
}

url = "https://jikipedia.com/"


# 每隔10秒钟执行
def t2():
    while 1:
        main()
        time.sleep(5)


def main():
    with open("JiKiPedia.json", "w", encoding='utf-8') as f:
        for k in range(100):
            try:
                res = requests.get(url=url, headers=headers, timeout=10)
                res.encoding = 'utf-8'
                selector = etree.HTML(res.text)
                card_xpath_reg = "//div[@class='lite-card container']"
                card = selector.xpath(card_xpath_reg)
                for i in card:
                    # 转成utf-8格式，然后decode进行encoding 指定的编码格式解码字符串
                    # print(etree.tostring(i, encoding='utf-8').decode())
                    title = ''.join(i.xpath(".//h1/*/text()"))
                    content = ''.join(i.xpath(".//div[@class='content text']/*//text()"))
                    img = ''.join(i.xpath(".//div[@class='card-middle divider']/div[@class='image']/img[@class='scaled card-image']/@src"))
                    author = ''.join(i.xpath(".//div[@class='author']/*//text()"))
                    like_content = ''.join(i.xpath(".//div[@class='like-count count text']/text()"))
                    obj = {'title': title, 'content': content, 'img': img, 'author': author, 'like_content': like_content}
                    f.write(json.dumps(obj, indent=2, ensure_ascii=False) + ",\n")
            except:
                continue


if __name__ == '__main__':
    print("一大波数据正在到碗里来~")
    t = threading.Thread(target=t2)
    t.start()
    t.join()
