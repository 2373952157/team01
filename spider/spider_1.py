import urllib.request as lib
from bs4 import BeautifulSoup

response = lib.urlopen("http://www.baidu.com")  # 打开相应一个HTML
txt = response.read().decode("utf-8")   # 读取HTML
f = open('xxx.html','w',encoding='utf-8')  # 打开一个文件，要是没有则创建
f.writelines(txt)  # 写入
f.close()  # 关闭

file = open('C:\\Users\赵轩\Desktop\大三下实训\spider\index2.html','rb')  # 文件应该放在总的project下，而不是project的子目录下
html = file.read()
bs =  BeautifulSoup(html,'html.parser')   # 可加,from_encoding="utf-8"
print(bs.title)  # 获取title所有标签的名称   显示： <title>百度一下，你就知道</title>
print(bs.prettify())  # 使用prettify能看起来更美观，即加了\n
print(bs.title.name)   # 获取title标签的所有内容  显示：title
print(bs.title.string)   # 获取title标签的文本内容   显示：百度一下，你就知道
print(bs.head)  # 获取head标签中的所有内容
print(bs.div)  # 获取第一个div标签中的所有内容  显示：<head>.*?</head> .*?代表省略
print(bs.div['id'])  # 获取第一个div标签的id的值  显示：wrapper
print(bs.a)  # 获取第一个a
print(bs.find_all("a"))  # 获取所有a标签中的所有内容
print(bs.find(id='u1'))   # 获取id=“u1”

for item in bs.find_all("a"):
    print(item.get('href'))   # 获取所有a标签，并遍历打印a标签的文本值

for item in bs.find_all("a"):
    print(item.get_text())  # 获取所有a中的文本

