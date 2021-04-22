import requests
from bs4 import BeautifulSoup
import re

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.72 Safari/537.36"
        }  # "Cookie":""

def Get_html(urls):  # 通过模仿浏览器发送请求HTML
    url = urls
    req = requests.get(url,headers=head)
    req.encoding = 'utf-8'
    html = req.text
    return html

def spiderurl(htmls):
    my_page = BeautifulSoup(htmls, 'html.parser')  # 解析
    global choices
    div_p = my_page.find('div', attrs={'class': "b-wrap g-cw cfx"})
    title = div_p.find_all('div',attrs={'class':'q-tit'})
    try:
        choices = div_p.find_all('div',attrs={'class':'exam-s'})
        print(choices)
    except:
        print('失败')
        pass
    answer = div_p.find_all('div',attrs={'class':'q-analyize top-analyze'})
    # print(choices)
    n = 0
    for i in title:
        title_photo_href = ''
        title_photo_href_p = '<img class="mathml" src="//(.*?)" sty.*?>'
        title_photo_href = re.findall(title_photo_href_p, str(i), re.S)
        a = re.sub('<img.*?middle;"/>','"插入图片"',str(i))
        a = re.sub('\\n','',str(a),re.S)
        a = re.sub('<div class="q-tit">','',a)
        a = re.sub('<a class=.*?">','',a)
        a = re.sub('</a>','',a)
        a = re.sub('</div>','',a)
        a = re.sub(' ','',a)
        print(a)
        b = []
        try:
            b = re.findall('src="(.*?) style=.*?', str(choices[n]), re.S)
            print('b:',b)
            if len(b) == 0:
                a = re.findall('<span class="op-item-meat">(.*?)</span></span>', str(choices[n]), re.S)
                print(a)
            else:
                print(b)
            n = n+1
        except:
            b = ['1', '2', '3', '4']
        print(title_photo_href)
        # print('图片个数',len(title_photo_href))
        # print('*'*20)
        f = open('ourself3.csv', mode='a', encoding='utf-8')
        f.write(a)
        f.write(',')
        for i in b:
            f.write(i)
            f.write(',')
        for i in title_photo_href:
            f.write(i)
            f.write(',')
        f.write('\n')


for i in range(3392725,3392726):
    try:
        html = Get_html('https://www.zujuan.com/paper/view-'+str(i)+'.shtml')
        spiderurl(html)
        print('第',i,'个成功')
    except:
        print('第',i,'个失败')

#3389200

# for i in choices:
#     # print(i)
#     b = re.findall('src="(.*?) style=.*?',str(i),re.S)
#     if len(b) == 0:
#         a = re.findall('<span class="op-item-meat">(.*?)</span></span>',str(i),re.S)
#         print(a)
#     else:
#         print(b)
#     print('---'*20)
