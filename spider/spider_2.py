import requests
import re
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 \
QQBrowser/10.5.3863.400'}
url = 'http://www.baidu.com'
res = requests.get(url, headers=headers,timeout=10).text
p_info = '<span class="title-content-title">(.*?)</span>'
info = re.findall(p_info,res,re.S)