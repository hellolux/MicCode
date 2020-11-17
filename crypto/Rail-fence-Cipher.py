# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/17 10:26
# @Function: 栅栏密码

import math

# 明文
C = " h e l l o w o r l d "
# 一行几个单词
N = 3
# 密文
M = "hlodeorlwl"

def encode(C,N):
    """
    栅栏加密
    :param C: 明文
    """
    # 去除空格
    C = ''.join(C.split())
    # 计算能切分为几行
    sum = math.ceil(len(C) / N)
    # 遍历生成字典
    MList = {}
    tmpStart = 0
    for i in range(sum):
        tmpEnd = tmpStart + N
        MList[i] = C[tmpStart:tmpEnd]
        tmpStart = tmpEnd
    # 生成密文
    M = ""
    for j in range(N):
        for i in range(sum):
            tmpLen = len(MList[i])
            if tmpLen > j:
                M += MList[i][j]
    print("明文:[ {} ] 行数:[ {} ] 密文:[ {} ]  ".format(C, N, M))

def decodeResult(M,N):
    """
    栅栏解密
    :param M: 密文
    :param N: 几列
    """
    # 去除空格
    M = ''.join(M.split())
    # 计算出有几列是最长的
    howLong = len(M) % N
    # 计算出最长的一列有几个元素
    longNum = math.ceil(len(M) / N)
    # 生成字典
    MList = {}
    tmpHow = 0
    tmpStart = 0
    for i in range(N):
        tmpEnd = tmpStart + longNum
        if tmpHow < howLong:
            tmpHow += 1
        else:
            if tmpHow != 0:
                tmpEnd -= 1
        MList[i] = M[tmpStart:tmpEnd]
        tmpStart = tmpEnd
    # 生成明文
    C = ""
    tmpHow = 0
    # 生成明文
    for i in range(longNum):
        for j in range(N):
            tmpLen = len(MList[j])
            if i >= tmpLen: continue
            else:C += MList[j][i]
    print("密文:[ {} ] 行数:[ {} ] 明文:[ {} ]".format(M,N,C))

def decode(M,N = 0):
    """
    栅栏解密
    :param M: 密文
    :param N: 行数
    """
    # 没有赋值行数，采用爆破法
    if N == 0:
        for N in range(len(M)):
            if N == 0 or N == 1: continue
            decodeResult(M,N)
    else:
        decodeResult(M,N)

encode(C,N)
decode(M,N)