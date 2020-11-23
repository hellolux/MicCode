# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/18 8:37
# @Function: 凯撒密码爆破

import sys,getopt

# 密文
M = 'FRPHEVGL'
N = ""
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

# for i in range(26):
#     if i == 0:continue
#     decode(M,i)

if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        print('请输入参数 -h 了解使用方法.')
        sys.exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hm:k:')
    except getopt.GetoptError:
        print('请输入参数 -h 了解使用方法.')
        sys.exit()
    for opt, arg in opts:
        if opt == "-h":
            print("功能: 凯撒密码暴力破解")
            print("使用: python Caser-Blasting.py -m <密文> [-k <>]")
            print("例子: python Caser-Blasting.py -m FRPHEVGL -k 13")
            sys.exit()
        elif opt == '-m':
            M = arg
        elif opt == '-k':
            N = arg
    if N == "":
        for i in range(26):
            if i == 0: continue
            decode(M,i)
    else:
        decode(M,int(N))