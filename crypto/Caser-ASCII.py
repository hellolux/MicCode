# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/18 9:16
# @Function: ASCII变种凯撒规律查询

import sys,getopt

def test(i,newTmp):
    """
    是否符合规律判断
    :param i: 元素下标
    :param newTmp: 新字符
    :return: 一致返回True，不一致返回False
    """
    global oldTmp
    if i == 0: oldTmp = newTmp
    if newTmp != oldTmp: return False
    return True

def TIOD(M,subTmp,TioTmp):
    """
    二次等差增减测试恢复明文
    :param M: 密文
    :param subTmp: 第一次等差额
    :param TioTmp: 第二次等差额
    :return:
    """
    C = ""
    for i in range(len(M)):
        tmp = ord(M[i]) + subTmp
        if tmp > 127: tmp = tmp - 127
        C += chr( tmp )
        subTmp += TioTmp
    print("--------")
    print("测试成功！")
    print("测试的明文为: {}".format(C))
    print("--------")

def main(M,G):
    """
    主函数
    :param M: 密文
    :param G: 起始猜想值
    """
    # 密文字典
    MDic = {}
    # 猜想字典
    GDic = {}
    # 一致性判断临时变量
    oldTmp = -999999999
    for i in range(len(G)):
        MDic[i] = ord(M[i])
        GDic[i] = ord(G[i])

    # 等差增减测试
    IODDic = {}
    # 测试标志
    FLAG = True
    for i in range(len(GDic)):
        IODDic[i] = GDic[i] - MDic[i]
        if not test(i, IODDic[i]): FLAG = False
    if not FLAG:
        print("一次等差增减测试结果为: {}".format(IODDic))
    else:
        TIOD(M, IODDic[0], 0)

    # 二次等差增减测试
    TIODDic = {}
    # 测试标志
    FLAG = True
    for i in range(len(IODDic) - 1):
        TIODDic[i] = IODDic[i + 1] - IODDic[i]
        if not test(i, TIODDic[i]): FLAG = False
    if not FLAG:
        print("二次等差增减测试结果为: {}".format(TIODDic))
    else:
        TIOD(M, IODDic[0], TIODDic[0])

if __name__ == '__main__':
    # 密文
    M = "afZ_r9VYfScOeO_UL^RWUc"
    # 猜想
    G = 'flag{'
    main(M,G)