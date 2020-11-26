# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/25 16:27
# @Function: 将TSV文件写入MYSQL数据库中

import pandas as pd
from sqlalchemy import create_engine
import sys,getopt
MYSQLUser = ""
MYSQLPass = ""
MYSQLIP = ""
MYSQLPort = ""
MYSQLDatabases = ""
MYSQLTables = ""
TsvFileName = ""

def tsvToMysql(MYSQLUser,MYSQLPass,MYSQLIP,MYSQLPort,MYSQLDatabases,MYSQLTables,TsvFileName):
    """
    读取TSV文件内容转存至数据库中
    :param MYSQLUser: MYSQL用户名
    :param MYSQLPass: MYSQL密码
    :param MYSQLIP: MYSQL的IP地址
    :param MYSQLPort: MYSQL端口
    :param MYSQLDatabases: MYSQL数据库名
    :param MYSQLTables: MYSQL表名
    :param TsvFileName: 待导入的tsv文件名
    """
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQLUser,MYSQLPass,MYSQLIP,MYSQLPort,MYSQLDatabases))
    train=pd.read_csv('{}'.format(TsvFileName), sep='\t', header=0)
    train.to_sql('{}'.format(MYSQLTables), engine, index=False)
    print("存储成功!")

if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        print('请输入参数 -h 了解使用方法.')
        sys.exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hu:m:i:p:d:f:t:',['help','user=','mima=','ip=','port=','databases=','file=','tables='])
    except getopt.GetoptError:
        print('请输入参数 -h 了解使用方法.')
        sys.exit()
    for opt, arg in opts:
        if opt == "-h":
            print("""
功能: 将TSV文件写入MYSQL数据库中
使用: python Tsv-To-MYSQL.py 
        -u/--user <MYSQL用户名> 
        -m/--mima <MYSQL密码> 
        -i/--ip <MYSQL的IP地址> 
        -p/--port <MYSQL端口> 
        -d/--databases <MYSQL数据库名> 
        -f/--file <待导入的tsv文件名> 
        -t/--tables <MYSQL表名,必须不存在的表>
例子: python Tsv-To-MYSQL.py -u root -m root -i localhost -p 3306 -d cn_chara -f zi-dataset.tsv -t zi_dataset
                """)
            sys.exit()
        elif opt in ('-u', '--user'):
            user = arg
        elif opt in ('-m', '--mima'):
            password = arg
        elif opt in ('-i', '--ip'):
            ip = arg
        elif opt in ('-p', '--port'):
            port = arg
        elif opt in ('-d', '--databases'):
            databases = arg
        elif opt in ('-t', '--tables'):
            tables = arg
        elif opt in ('-f', '--file'):
            files = arg
    tsvToMysql(user,password,ip,port,databases,tables,files)
