def fib(n):
    a, b = 1, 1
    while a<n:
        print(a,end=' ')
        a,b = b, a+b
    print()
fib(1000)

def fib(n):
    '''
    accept an interger n.
    return the numbers less than n in Fibonacci sequence
    '''
    a, b =1, 1
    while a<n:
        print(a, end=' ')
        a, b = b, a+b
    print()


help(fib)

a_list = [1,2,3,9,7,4,5]
print(sorted(a_list))
print(a_list.sort())   # 列表对象的sort()方法没有放回值

def linear(a,b):
    def result(x):
        return a * x +b
    return result

class linear:
    def __init__(self,a,b):
        self.a, self.b = a,b
    def __call__(self, x):
        return self.a * x + self.b

taxes = linear(0.3, 2)  # 调用对象
taxes(5)



def check_permission(func):
    def wrapper(* args, ** kwargs):
        if kwargs.get('username')!= 'admin':
            raise Exception('Sorry. You are not allowed.')
        return func(* args, ** kwargs)
    return wrapper

class ReadWriteFile(object):
    # 把函数check_permission作为装饰器使用
    @ check_permission
    def read(self, username, filename):
        return open(filename,'r').read()

    def write(self,username,filename,content):
        open(filename,'a+').write(content)
    # 把函数check_permission作为普通函数使用
    write = check_permission(write)

t=ReadWriteFile()
print('Originally……')
print(t.read(username='admin',filename=r'c:\Users\赵轩\Desktop\32.txt'))
print('Now, try to write to a file……')
t.write(username='admin',filename=r'c:\Users\赵轩\Desktop\32.txt',content='\nhello world')
print('After calling to write……')
print(t.read(username='admin',filename=r'c:\Users\赵轩\Desktop\32.txt'))


def say(message, times=1):
    print((message+' ')*times)
say.__defaults__  # 这个不能用say.func_defaults
say('hello')
say('hello',3)

def demo(newitem, old_list=[]):
    old_list.append(newitem)
    return old_list
print(demo('5',[1,2,3,4]))
print(demo('aaa',['a','b']))

def demo(*p):
    print(p)
demo(1,2,3)

def demo(**p):
    for item in p.items():
        print(item)
demo(x=1,y=2,z=3)

def demo(a,b,c):
    print(a,b,c)
seq = [1,2,3]
demo(*seq)
dic = {1:'a',2:'b',3:'c'}
demo(*dic)
demo(*dic.values())
demo(*(3,),**{'c':1,'b':2})  # 一个 * 会在 ** 前处理


def demo():
    global x
    x = 3
    y = 4
    print(x,y)
x = 5
demo()
x

def scope_test():
    def do_local():
        spam='我是局部变量'

        def do_nonlocal():
            nonlocal spam
            spam="我不是局部变量，也不是全局变量"

        def do_global():
            global spam
            spam = "我是全局变量"

        spam = "原来的值"
        do_local()
        print("局部变量赋值后:",spam)
        do_nonlocal("nonlocal变量赋值后:",spam)
        do_global()
        print("全局变量赋值后:",spam)

scope_test()
print("全局变量",spam)

