from bs4 import BeautifulSoup
import requests
import time

req = requests.get('http://58921.com/alltime/')  # 获取url
req.encoding = 'utf-8'
my_Page = BeautifulSoup(req.text,'html.parser')   # 解析
table = my_Page.find('table',attrs={'class':"center_table movie_box_office_stats_table table table-bordered table-condensed"})  # 找table标签，添加attrs条件
trs = table.find_all("tr")  # 返回tr的一个元组,每一行
# print(table.text)  查看table里的所有内容
f = open('piao.csv',mode='a',encoding='utf-8')  # mode = 'a' 追加模式
for tr in trs:  # 遍历所有行
    tds = tr.find_all('td')    # 返回所有列
    for td in tds:   # 遍历所有列
        # print(td)  # 查看每一行
        f.write(td.text.strip())
        f.write(',')
    # print('\n')  # 每一
    f.write('\n')
print('Done!')
f.close()  # 关闭文件


# 集成
def P_year(year):
    req = requests.get('http://58921.com/alltime/{}'.format(year))  # or 'http://58921.com/alltime/' + year
    req.encoding = 'utf-8'
    my_Page = BeautifulSoup(req.text, 'html.parser')  # 解析
    table = my_Page.find('table', attrs={
        'class': "center_table movie_box_office_stats_table table table-bordered table-condensed"})  # 找table标签，添加attrs条件
    trs = table.find_all("tr")  # 返回tr的一个元组,每一行
    # print(table.text)  查看table里的所有内容
    f = open('piao2.csv', mode='a', encoding='utf-8')  # mode = 'a' 追加模式
    f.write(str(year))
    f.writelines('年')
    for tr in trs:  # 遍历所有行
        tds = tr.find_all('td')  # 返回所有列
        for td in tds:  # 遍历所有列
            # print(td)  # 查看每一行
            f.write(td.text.strip())
            f.write(',')
        # print('\n')  # 每一
        f.write('\n')
    print('Done!')
    f.close()  # 关闭文件
for year in range(2010,2021):   # 遍历爬取2010-2020年的数据
    P_year(year)  # 调用函数
    time.sleep(20)  # 定义响应时间，超过则跳过