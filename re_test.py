import re
# 1. re.split
text = 'alpha.beta...gamma delta'
re.split('[\. ]+',text)  # 使用指定字符串作为分隔符进行分隔
re.split('[\. ]+',text,maxsplit=2)  # 最多分隔两次
re.split('[\. ]+', text ,maxsplit=1)  # 最多分隔一次
# 2. re.findall
pat = '[a-zA-z]+'
re.findall(pat,text)  # 查找所有单词  输出：['alpha', 'beta', 'gamma', 'delta']
# 3. re.sub
pat = '{name}'
text ='Dear {name}...'
re.sub(pat,'Mr.Dong',text) # 输出：'Dear Mr.Dong...'
s = 'a s d'
re.sub('a|s|d','good','s')  # 输出：'good'
# 4. re.escape
re.escape('http://www.python.org') # 输出：'http://www\\.python\\.org'
# 5. re.match
print(re.match('done|quit','done'))  # 匹配成功则返回match对象
print(re.match('done|quit','done!'))  # 匹配成功
print(re.match('done|quit','doe!'))  # 匹配不成功，返回None
print(re.match('done|quit','done!'))
print(re.match('done|quit','quitd'))  # 匹配成功
print(re.match('done|quit','quit！！d')) # 匹配成功
print(re.match('done|quit','!quitd'))  # 匹配不成功
# 6. re.search
print(re.search('done|quit','d!one!done'))  # 匹配成功

s = 'aaa    bb    c d e   fff   '
' '.join(s.split())  # 不使用正则表达式,直接使用字符串对象的方法,输出：'aaa bb c d e fff'
re.split('[\s]+',s)  # \s匹配任何空白字符，包括空格、制表符、换页符，输出：['aaa', 'bb', 'c', 'd', 'e', 'fff', '']
s.strip() # 清除；两端空格，输出'aaa    bb    c d e   fff'
' '.join(re.split('[\s]+',s.strip())) # 输出：'aaa bb c d e fff'
' '.join(re.split('\s+',s.strip())) # 输出：'aaa bb c d e fff'
re.sub('\s+', '',s.strip())  # 输出：'aaabbcdefff'

example = 'ShanDong Institude of Business and Technology is a very beautiful school.'
re.findall('\\ba.+?\\b',example) # \b表示匹配单词头或单词尾,以字母a开头的完整单词,输出:['and', 'a ']
re.findall('\\ba\w*\\b',example) # \w匹配任何字母、数字以及下划线,输出:['and', 'a']
re.findall('\\Bo.+?\\b',example) # 输出：['ong', 'ology', 'ool']
re.findall('\\b\w.+?\\b',example)  # 所有单词
re.findall('\w+',example)  # 所有单词
re.findall(r'\b\w.+?\b',example)  # 使用原始字符串
re.split('\s',example)  # \s匹配任何空白字符
re.findall('\d+\.\d+\.\d+','Python 2.7.11')  # 输出：['2.7.11']
re.findall('\d+\.\d+\.\d+','Python 2.7.11,Python 3.5.1')  # 输出:['2.7.11', '3.5.1']

example = 'ShanDong Institude of Business and Technology'
pattren = re.compile(r'\bB\w+\b')  # 查找以B开头的单词
pattren.findall(example)  # 输出：['Business']
pattren = re.compile(r'\w+g\b')  # 查找以字母g结尾的单词
pattren.findall(example) # 输出:['ShanDong']
pattren = re.compile(r'\b[a-zA-Z]{3}\b') # 查找3个字母长的单词
pattren.findall(example)  # 输出：['and']
pattren.match(example)  # 从字符串开头开始匹配，失败则返回空值
pattren.search(example)   # 在整个字符串中搜索，成功
text = 'He was carefully disguise but captured quickly by police'
re.findall(r'\w+ly',text)   # 输出：['carefully', 'quickly']

example='''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''
pattren = re.compile(r'\bb\w*\b',re.I)
pattren.sub('*',example)  # 将符合条件的单词替换为*
pattren.sub('*',example,1) # 只替换1次
pattren = re.compile(r'\bb\w*\b')
pattren.sub('*',example,1)

example = r'one,two,three.four/five\six?seven[eight]nine|ten'
pattren = re.compile(r'[,./\\?[\]\|]')
pattren.split(example)  # 输出：['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
example = r'one1two2three3four4five5six6seven7eight8nine9ten10'
pattren = re.compile(r'\d+')
pattren.split(example)
example = r'one two   three   four,five.six.seven,eight,nine9ten'
pattren = re.compile(r'[\s,.\d]+')
pattren.split(example)

# match
email = 'tony@tiremove_thisger.net'
m = re.search("remove_this",email)
email[:m.start()]+email[m.end():]  # 输出：'tony@tiger.net'
re.sub('remove_this','',email) # 输出：'tony@tiger.net'
email.replace('remove_this','') # 输出：'tony@tiger.net'
m = re.match(r"(\w+) (\w+)","Isaac Newton,physicist")
m.group(0)  # 输出：'Isaac Newton'
m.group(1)  # 输出：'Isaac'
m.group(2)  # 输出: 'Newton'
m.group(1,2)  # 输出：('Isaac', 'Newton')