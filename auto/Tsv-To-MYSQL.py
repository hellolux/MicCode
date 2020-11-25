# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/25 16:27
# @Function: 将TSV文件写入MYSQL数据库中

import pandas as pd

# 读取tsv文件
train=pd.read_csv('test.tsv', sep='\t', header=0)
sqlStr = "INSERT INTO zi-dataset "
colStr = ""
valStr = ""
colFlag = False
# 获取列名
for i in range(len(train)):
    if not colFlag: colStr += "( "
    valStr += "( "
    for j in train:
        if not colFlag:  colStr += j + ","
        valStr += "'" + str(train[j][i]) + "',"
        # print("i: {} j: {} val: {}".format(i,j,train[j][i]))
    if not colFlag:
        colStr = colStr[:-1]
        colStr += ")"
    valStr = valStr[:-1]
    valStr += "),"
    colFlag = True
# print(colStr)
valStr = valStr[:-1]
sqlStr = sqlStr + colStr + " VALUES " + valStr
print(sqlStr)