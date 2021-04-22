from bs4 import BeautifulSoup  #解析获取的html页面
import requests
import time

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
        "Cookie":"HMACCOUNT_BFESS=012C8CE509A60059; BDUSS_BFESS=DVGN35WdGtWdU5Tb1ZHS29uajd4enM1MVNwTGtRTHpMRDJSS3JOZzcxdjAxbXBnRVFBQUFBJCQAAAAAAAAAAAEAAACidCGf1-3J7bmr19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPRJQ2D0SUNgc; BAIDUID_BFESS=F850EDDDBAA5769967C70FC19BD895AC:FG=1"}


def P_year(year,num):
    req = requests.get('http://58921.com/alltime/'+year+'?page='+num,headers = head)
    #或者写成’http://**** + year‘
    req.encoding = 'utf-8'
    my_page = BeautifulSoup(req.text,'html.parser')  #解析
    table = my_page.find('table',attrs={
        'class':"center_table movie_box_office_stats_table table table-bordered table-condensed"})
    try:
        trs = table.find_all("tr")
        #返回tr的一个元组，每一行6
        #print(table.text) 查看table里的所有内容
        f = open('piao5.csv',mode ='a',encoding ='utf-8')  #mode = 'a' 追加模式    f.write(str(year))
        f.writelines('年')
        for tr in trs:  #遍历所有行
            tds = tr.find_all('td')  #返回所有列
            for td in tds:  #遍历所有列
                f.write(td.text.strip())  #查看每一行
                f.write(',')  #csv默认以逗号分隔数据
            f.write('\n')
        print('Done!')
        f.close()
    except:
        print('wrong')


for year in range(2010,2021): #遍历爬取2010-2020年的数据
    for num in range(0,8):
        P_year(str(year),str(num))
    #P_year(year)  #调用函数
    time.sleep(2)  #定义响应时间，超过则跳过
    # P_year(str(year)+"?page=1") #继续爬取同一年、第二页（？page=1）的数据


