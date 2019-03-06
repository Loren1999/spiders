import requests
from lxml import etree
from fake_useragent import UserAgent
import MySQLdb as mysql


def get_random_ua():  # 随机UA
    ua = UserAgent()
    return ua.random


headers = {
    'User-Agent': get_random_ua()
}

url = 'https://www.nihaowua.com/'


def main():
    count = 0
    # get connect
    con = mysql.connect(host="localhost", user="root", passwd="password", db="spiders", charset='utf8')
    for k in range(50000):
        try:
            cursor = con.cursor()
            sql = "insert into content(content) values"
            for i in range(10):
                # get content from internet
                res = requests.get(url=url, headers=headers, timeout=10)
                res.encoding = 'utf-8'
                selector = etree.HTML(res.text)
                xpath_reg = "//section/div/*/text()"
                results = selector.xpath(xpath_reg)
                content = results[0]

                # print sql
                if i <= 8:
                    sql = sql + "(" + "'" + content + "'" + ")" + ","
                else:
                    sql = sql + "(" + "'" + content + "'" + ")" + ";"
                # print(sql)
            count += 1
            cursor.execute(sql)
            cursor.close()
            con.commit()
            print('********数据入库中，这是第{}次入库********'.format(count))
        except:
            continue
    con.close()


if __name__ == '__main__':
    main()
