"""
回归分析法
根据《深度学习的数学》（图灵图书）——涌井良幸; 涌井贞美.
题目：
根据高三女生的身高体重数据，求回归方程y=px+q(p、q为常数)
1、153.3、45.5
2、164.9、56.0
3、168.1、55.0
4、151.5、52.8
5、157.8、55.6
6、156.7、50.8
7、161.1、56.4
"""

# 预测值 yk = 153.3p+q
# 预测值的误差 ek = yk - (p * xk + q)
# 平方误差 ck = 1 / 2 * (ek ^ 2)
# 所有数据的平方误差和 ct = c1 + c2 + ... + ck
# 利用最小值条件，求出dct / dp = 0; dct / dq = 0
# dct/dp = dct/du * du/dp
# 将1 / 2 * (ek ^ 2) 看成整体求导等于 ek
# 将ek求导等于-p
# dct/dp = -p1 * e1 + ... -pk * ek
# dct/dq = -1 * e1 + ... -1 * ek

from sympy import *
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 定义变量
p = Symbol('p')
q = Symbol('q')
# 定义数据
height = [153.3, 164.9, 168.1, 151.5, 157.8, 156.7, 161.1]
weight = [45.5, 56.0, 55.0, 52.0, 55.6, 50.8, 56.4]
# 定义常量
DctDpX = 0.0
DctDpP = 0.0
DctDpQ = 0.0
DctDQX = 0
DctDQP = 0
DctDQQ = 0

# 计算常量
# DctDpX = -1 * height * weight
# DctDpP = pow(height,2)
# DctDpQ = height
#
# DctDQX = -1 * weight
# DctDQP = height
# DctDQQ = 1

for i in range(len(height)):
    # 计算常量
    tmp = height[i] * weight[i]
    DctDpX += -1 * tmp
    DctDpP += pow(height[i], 2)
    DctDpQ += height[i]

    DctDQX += -1 * weight[i]
    DctDQP += height[i]
    DctDQQ += 1


print("求出DCT/DP = %s + %s * P + %s * Q" % (DctDpX, DctDpP, DctDpQ))
print("求出DCT/DQ = %s + %s * P + %s * Q" % (DctDQX, DctDQP, DctDQQ))
res = solve(
    [
        DctDpX + DctDpP * p + DctDpQ * q,
        DctDQX + DctDQP * p + DctDQQ * q
    ],
    [p,q]
)
print("p: %s, q: %s" % (res[p], res[q]))

plt.scatter(height,weight,label='原始数据')
x = np.arange(150,170,1)
y = res[p] * x + res[q]
plt.plot(x, y,label='回归函数')
plt.legend()
plt.show()