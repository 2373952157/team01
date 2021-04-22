import numpy as np
np.linspace(1,11,4)   # 生成 4 个数
np.random.randint(2,9,size=(3,3))
np.arange(1,10,2,dtype=float)
np.logspace(1,stop=4,endpoint=True,base=2)  # base 函数的底数, endpoint 为 True 则包含 stop
np.diag([1,2,3]) # 对角线
np.eye(5)  # 5 * 5 的对角矩阵
np.zeros(5)
np.ones(2)
np.random.rand(10)  # 均态分布
np.random.randn(10)  # 正态分布
np.random.randn(1,5)
a1 = np.random.randint(2,9,size=(3,3))
a2 = np.random.randint(3,10,size=(3,3))
np.hstack([a1,a2])
np.vstack([a1,a2])
np.concatenate([a1,a2],axis=1)  # axis = 1 ，代表横向
np.hsplit(a1,3)  # 横向分割
np.vsplit(a1,3)  # 纵向分割
a1[:,0]  # 所有行，第 0 列
a1.flatten()  # 展开
a1.flatten('F')  # 展开
a1.ravel()  # 展开
np.random.randint(1,10)
a1
np.save('np_file',a1)
np.load('np_file.npy')
np.sort(a1)

# matplotlib
# 1.创建画布
# 2.是否创建子图
# 3.选定子图
# 4. 标题、X轴、修改X轴刻度与范围、添加y轴、修改y轴刻度
# 5.绘制图形
# 6.修改图例
# 7.保存图形
# 8.显示图形
import matplotlib.pyplot as plt
import numpy as np
plt.figure(num=7,figsize=(8,6))  # num编号 ，不加则自然增长
plt.suptitle('all title')

# 第 1 个图
ax1 = plt.subplot(221) # 2行2列第一个
plt.xlim(-5,5)  # x 坐标 -5 到 5
x = np.arange(0,3,0.5)  # 以3为步长
y = np.sin(x)
plt.plot(x,y)
ax1.set_title('title1',loc='left')

# 第 2 个图
ax2 = plt.subplot(222)  # 2行2列第2个
# plt.xlim(-1,1)
x_2  =  np.arange(200,300)
y_2  =  np.cos(x_2)
plt.plot(x_2,y_2)
ax2.set_title('title2',loc='right')

# 第 3 个图
ax3 = plt.subplot(212)  # 2行1列第2个
# plt.xlim(-10,5)
a=np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
ax3.set_title('title',loc='center')

plt.show()