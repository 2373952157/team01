import requests
from bs4 import BeautifulSoup
import time
import random

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}


def Get_html(urls):  # 通过模仿浏览器发送请求HTML
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
    url = urls
    req = requests.get(url,headers=header)
    req.encoding = 'utf-8'
    html = req.text
    return html

def Get_data(htmlCode):
    soup = BeautifulSoup(htmlCode, 'html.parser')
    items = soup.find_all('div',class_="item")

    data_all = []
    for item in items:
        data = []
        # 链接
        link = item.find('a').get('href')
        data.append(link)
        # 图片
        global img
        img = item.find('img').get('src')                #图片地址
        data.append(img)
        savePIG(img)
        # 内容
        hd = item.find('div',attrs={'class':'hd'})
        title = hd.find_all('span',attrs={'class':'title'})
        other = hd.find('span',attrs={'class':'other'})

        name = ''
        if len(title) == 2:
            name = title[0].text.replace(',',' ') + title[1].text.replace(',',' ')
        else:
            name = title[0].text.replace(',',' ')
        data.append(name)
        data.append(other.text)
        # print(data)

        bd = item.find('div',attrs={'class':'bd'})
        actor = bd.find('p').text.strip()
        actor = actor.replace('\n','')
        spans = bd.find_all('span')

        rating = spans[1].string  # 评分
        evalute = spans[3].string  # 评价

        try:
            inq = spans[4].string  # 简评
        except:
            inq = ''  # 因为有些没有简评
            pass

        # print(actor)
        # print(spans)
        data.append(actor)
        data.append(rating)
        data.append(evalute)
        data.append(inq)
        # print(data)
        data_all.append(data)
    return data_all
    # print(data_all)

def save_file(data):
    f = open('movie（1）.csv',mode='a',encoding='utf-8')
    for i in range(len(data)):
        for j in range(len(data[i])):
            f.write(data[i][j])
            f.write(',')
        f.write('\n')
    f.close()

def savePIG(url):
    number = int(random.random()*10000000)
    f = open("./img/"+ str(number)+".jpg", mode="wb")
    resp = requests.get(url,headers =header,timeout = 15)
    f.write(resp.content)
    resp.close()
    f.close()
    print("SavePIG!")

for i in range(0,26,25):
    htmlCode = Get_html('https://movie.douban.com/top250?start='+str(i))
    data_all = Get_data(htmlCode)
    save_file(data_all)
    time.sleep(1)
print('done!')

