"""
梯度下降算法
根据《深度学习的数学》（图灵图书）——涌井良幸; 涌井贞美.
书中的用Excel体验梯度下降法用Python进行实现

题目：
对于函数z = x^2 + y^2，用梯度下降算法求出使得函数取得最小值的x,y的值
"""
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

"""
初始设定函数
"""
# 设定学习率n
n = 0.1
# 设置初始位置
x = 3
y = 2
# 设置下降次数
sum = 31
# 坐标记录
Ax = []
Ay = []
# 梯度记录
Bx = []
By = []
# 位移向量记录
Cx = []
Cy = []
# 函数值记录
Zx = []
Zy = []

for num in range(sum):
    # 保存坐标
    Ax.append(x)
    Ay.append(y)
    # 计算梯度
    dzdx = 2 * x
    dzdy = 2 * y
    # 保存梯度
    Bx.append(dzdx)
    By.append(dzdy)
    # 计算位移向量
    Dx = -1 * n * dzdx
    Dy = -1 * n * dzdy
    # 保存位移
    Cx.append(Dx)
    Cy.append(Dy)
    # 计算函数值
    z = pow(x,2) + pow(y,2)
    # 保存函数
    Zx.append(num)
    Zy.append(z)
    # 打印结果
    print("步数：{} 坐标: ({},{}) 梯度：({},{}) 位移向量:({},{}) 函数值:{}".format(num, round(x,2), round(y,2), round(dzdx,2), round(dzdy,2), round(Dx,2), round(Dy,2), round(z,2)))
    # 更新坐标
    x = x + Dx
    y = y + Dy
    # 步数增加
    num += 1
# 绘制坐标
plt.plot(Ax, Ay, 'x-', label='坐标')
plt.plot(Bx, By, 'D-', label='梯度')
plt.plot(Cx, Cy, 'd-', label='向量')
plt.plot(Zx, Zy, '+-', label='函数值')
plt.legend()
# 生成坐标图
plt.show()
