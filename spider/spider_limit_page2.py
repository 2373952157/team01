from bs4 import BeautifulSoup
import requests

def P_year_2(year):
    for i in range(2):
        req = requests.get('http://58921.com/alltime/'+year+'?page='+str(i))
        req.encoding = 'utf-8'
        my_Page = BeautifulSoup(req.text, 'html.parser')  # 解析
        try:
            table = my_Page.find('table', attrs={
                'class': "center_table movie_box_office_stats_table"
                         " table table-bordered table-condensed"})  # 找table标签，添加attrs条件
            trs = table.find_all("tr")  # 返回tr的一个元组,每一行
            f = open('piao3(2).csv', mode='a', encoding='utf-8')  # mode = 'a' 追加模式
            f.write(str(year));f.writelines('年');f.write(str(i+1));f.write('页')
            for tr in trs:  # 遍历所有行
                tds = tr.find_all('td')  # 返回所有列
                ths = tr.find_all('th')
                if len(tds) <=1 :
                    for th in ths:
                        f.write(th.text.strip())
                        f.write(',')
                for td in tds:  # 遍历所有列
                    # print(td)  # 查看每一行
                    f.write(td.text.strip())
                    f.write(',')
                # print('\n')  # 每一
                f.write('\n')
            print('Done!')
            f.close()  # 关闭文件
        except:
            pass
for year in range(1983,2021):  # 遍历爬取2010-2020年的数据
    P_year_2(str(year))  # 调用函数


'''def P_year_2(year):
    req = requests.get('http://58921.com/alltime/'+year)
    req.encoding = 'utf-8'
    my_Page = BeautifulSoup(req.text, 'html.parser')  # 解析
    try:
        table = my_Page.find('table', attrs={
            'class': "center_table movie_box_office_stats_table"
                     " table table-bordered table-condensed"})  # 找table标签，添加attrs条件
        trs = table.find_all("tr")  # 返回tr的一个元组,每一行
        f = open('piao4.csv', mode='a', encoding='utf-8')  # mode = 'a' 追加模式
        if 'page=1' not in year:
            f.write(str(year));f.writelines('年')
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
    except:
        pass
for year in range(1983,2021):  # 遍历爬取2010-2020年的数据
    P_year_2(str(year))  # 调用函数
    P_year_2(str(year)+'?page=1')  # 调用函数'''