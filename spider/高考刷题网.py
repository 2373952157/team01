import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
           'Cookie':
               'PHPSESSID=r7ucm49olv1uedei823u0u5ejd; __tins__20420247=%7B%22sid%22%3A%201618803019981%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201618804819981%7D; __51cke__=; __51laig__=1; Hm_lvt_6a1d64a2f26d241ce1901bb66d81466d=1618285079,1618295081,1618803020; nf_pepuser=%2582%255D%259C%259A%25A5%25EE%25E6%25AFcelU%258D%25A9%25DD%25B6%25AD%25C1%25E7%25D4%25BF%25D5%25CE%2586%2586%25DF%258C%25A6%25E6%25AD%25A6lSkUe%25A7%25A5uz%258D%2595%25C4%25BF%25E5%25D6%2586%2591%25DF%25CC%25CC%25E6%25DC%25D8Tl%25A5m%255Bn%258D%257Dj%258E%25E6%259B%257B%25A9%259EC%2596%25D0%25DD%25DE%25DC%25E2%25E3%25A6%259A%259F%2598%2596%259D%25D8%25AD%25BCu%25AE%25CA%2584%25A4%259AR%255B%25A3%259A%259E%25A3%25A5%25ACm%25A4ld%255Dn%258D%25B7%25AD%25C6%25E6%25CA%25B9%25E1%25D9%2594%2588%25DD%25D3%25CF%2595%25AE%25E8lelU%255Bd%25A0yj%258E%25E6%259B%257B%25A8%259EC%2596%25D0%25DD%25DE%25DC%25E2%25E3%25A2%2592%25A5%25A6%25A1%25A3%25DD%25A8j%258E%25E6%259B%257D%25A5%259EC%255B%25CF%25CF%25CC%25A3%25A8%25D6%2596a%2598lZl%259Fzx%258C%25D9%25C3%25AB%25A6%2597Z%2584%259D%25A2%259C%25A4%25D5%25ACj%2593Tn%259Dn%25A4%257Ej%25C6%25D8%25D4%25BD%25DC%25D3%258F%258C%25DB%258C%25A6%25E6%25AD%25A6ckThcb%25A1%257Cv%2589%25A4%258F%257B%25A6%2586%255C%2596%25A5%259B%25A1%25AD%2595%25E8%2597%25A4%25A5%259C%2599%25A2%25D2%25B6%25B7%25C8%25E3%25C4%25B9%25D7%25C9C%255E%25DE%25A4%259F%25AD%2595%25EA%25A5%2596%25A4Ue%25A7%25A5u%257E%258D%2595%25D4%25AF%25E6%25D7%258A%2592%25D9%25D6%25DA%25DA%25DC%25E3%25A6%259A%259F%2598Lo%25D4%257Ey%2589%25A4%2599%257C%25AC%2599RS%25A2%25A5%25DE%25AD%25A4%25AAlS%25A5%2598%259D%25A7%25D4%25B3%25B6%25C8%25E6%25C6%25BC%25E1%25C5%258E%2588%258D%25A5%25DE%25AD%25A4%25ABlS%25A9%25AB%2589j%259B%257B%257D%2586%25AC%2595%257B%25D4%259C%2583%2589%25CF%258C%25A6%25E6%25AD%25AElS%25A5%2598%259D%25A7%25D4%25B3%25B6%25BC%25D7%2583%2585%25E6%259ETU%25A5%258C%25A1%25AA%25D5%25D8d%2595%2594%2595a%2597%25A1z%2581%2588%25D9%2593%25B0%25D8%25C6%2583S%25CD%25CF%25CC%25AA%25A4%25A8cge%2599%255CV%25A6%25C1; Hm_lpvt_6a1d64a2f26d241ce1901bb66d81466d=1618803055'
           }

def saveFile(data,name):
    f = open('英语.csv',mode='a',encoding='utf-8')
    for i in data:
        f.write(str(i))
        f.write(',')
    f.write(name)
    f.write('\n')
    f.close()

def savePIG(url,name):
    f = open("./英语/"+ name, mode="wb")
    resp = requests.get(url,headers =headers,timeout = 15)
    f.write(resp.content)
    resp.close()
    f.close()

for i in range(1,31):
    try:
        url = 'https://gz.shuatiw.com/index.php?exam-app-point&questype=&pointid=21&number='+ str(i)
        req = requests.get(url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        main = soup.find('div',attrs={'class':'col-xs-9 nopadding'})
        item = soup.find('div',attrs={'class':'panel-body'})
        title = item.find('div',attrs={'class':'panel-heading'}).text  # 题目
        ABCD = main.find_all('p')  # 选项+解析
        real_daan = main.find('span',attrs={'class':'text-success'}).text  # 正确答案

        list = []
        list.append(title.strip())
        for j in ABCD[:-1]:
            list.append(str(j).strip('<p>|</p>'))
        list.append(real_daan)
        jiexi = re.findall('src="(.*?png)',str(ABCD[-1]))
        # savePIG(jiexi)
        list.append('https://gz.shuatiw.com'+''.join(jiexi))
        png_name = ''.join(jiexi)[-8:]
        saveFile(list,png_name)
        savePIG('https://gz.shuatiw.com'+''.join(jiexi),png_name)
        print('第',i,'个成功！！！')
    except:
        print('第',i,'个失败')
        pass


    # print('题目:',title.strip())
    # for i in ABCD[:-1]:
    #     print(str(i).strip('<p>|</p>'))
    # print('正确答案:',real_daan)
    # print('解析',ABCD[-1])
    # print('----'*30)
    # print(list)

print('over')

