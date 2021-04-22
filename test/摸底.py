''' 摸底 '''

'''1. 用户输入一个整数，用if...else判断是偶数还是奇数?
 示例：def  isOddEven():
	......

          # isOddEven
'''

def isOddEven():
    n = eval(input('请输入一个整数'))
    if (n%2 == 0):
        print('这是一个偶数')
    else:
        print('这是一个奇数')
isOddEven()

'''2.输入一个字母，判断是大写还是小写字母'''
def test_2():
    n = input('请输入一个字母')
    try:
        if (65<=ord(n)<=122):
            if 122 >= ord(n) >= 97:
                print('小写')
            else:
                print('大写')
    except:
        print('输入错误')
test_2()


'''3.求1~99所有奇数的和，用while语句  2500 '''
def test_3():
    s = 0
    i = 1
    while True:
        s += i
        i += 2
        if i > 100:
            break
    print(s)
test_3()



'''4.用户输入三个整数，将最大数和最小数输出?'''
def test_4():
    n_1 = input('请输入第一个整数')
    n_2 = input('请输入第二个整数')
    n_3 = input('请输入第三个整数')
    list = []
    list.append(n_1)
    list.append(n_2)
    list.append(n_3)
    print('最大数',max(list))
    print('最小数',min(list))
test_4()


'''5.输入三个数，按从小到大的顺序排列?'''
def test_5():
    n_1 = eval(input('请输入第一个数'))
    n_2 = eval(input('请输入第二个数'))
    n_3 = eval(input('请输入第三个数'))
    list = []
    list.append(n_1)
    list.append(n_2)
    list.append(n_3)
    print('按从小到大的顺序排列',sorted(list))
test_5()



'''6.将1~200末位数为5的整数求和  2000'''
def test_6():
    s = 0
    for i in range(0,201,5):
        if i % 2 == 0:
            pass
        else:
            s += i
    print(s)
test_6()



'''7.计算2.5的3次方'''
def test_7():
    print(2.5**3)
test_7()

'''8.将24的所有因子求积  13824'''
def test_8():
    s = 1
    for i in range(1,24):
        if (24%i==0):
            s = s*i
    print('24的所有因子求积为：',s)
test_8()

'''9.输入一段字符判断是大写，还是小写。若是小写，转换为大写，若是大写，转换为小写'''
def test_9():
    n = input('请输入一段大小写一致的字符')
    if n.islower():
        print(n.upper())
    else:
        print(n.lower())
test_9()

'''10.判断一个数是否为素数（质数）'''
def test_10():
    n = eval(input('请输入一个数'))
    for i in range(2,n):
        s = n%i
        if n%i ==0:
            print(n,'不是素数')
            break
    if s != 0:
        print(n,'这是一个素数')
test_10()

'''
11.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
因为153 = 1的三次方＋5的三次方＋3的三次方。
'''
def test_11():
    list = []
    for i in range(1,1000):
        x_1 = i//100
        x_2 = i//10 - i//100*10
        x_3 = i%10
        if i == (x_1**3 + x_2**3 + x_3**3):
            list.append(i)
test_11()

'''12.输入一个圆的直径，求它的周长和面积。'''
def test_12():
    import math
    n = eval(input('请输入圆的直径'))
    line = n * math.pi
    area = math.pi * ((n/2)**2)
    print('周长等于:',line)
    print('面积等于:',area)
test_12()

'''13.输入一个数，判断它是否同时被3和5整除。'''
def test_13():
    n = eval(input('请输入一个数'))
    if (n%3==0) and (n%5==0):
        print('它能同时被3和5整除')
    else:
        print('它不能同时被3和5整除')
test_13()


'''14.输入a，b，c的值。求? ax * x + bx + c = 0的根。'''
import math
# a = input()
# b = input()
# c = input()
# ax * x + bx +c =0
# x*x-2x+1 = 0


'''15.冒泡排序法。 '''
n = [1,3,2,5,4,7,8,6,9]
for i in n:
    for j in (i,n):
        print(i)





