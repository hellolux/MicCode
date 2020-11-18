# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/18 8:37
# @Function: 凯撒密码爆破

# 密文
M = 'FRPHEVGL'

def decode(M,N):
    # 明文
    C = ""
    # 遍历字符串解密
    for i in range(len(M)):
        tmp = ord(M[i]) - N - 65
        if tmp < 0:
            C += chr(91 + tmp)
        else:
            C += chr(ord(M[i]) - N)
    print("密文:[ {} ] 偏移量:[ {} ] 明文:[ {} ]".format(M,N,C))

for i in range(26):
    if i == 0:continue
    decode(M,i)