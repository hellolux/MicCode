# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Function: CRC32爆破


import binascii
import time

# 设定需要爆破的CRC32值
crcNum = {0x53A610F4, 0x0F9C4BBD, 0x0AAE6F9E}
# 设定CRC32的长度
crcLen = 5
# 设定ASCII码起始值
startASCII = 65
# 设定ASCII码结束值
endASCII = 91
# 设定爆破记录起始时间
startTime = time.perf_counter()

def checkCRC32(txt):
    """
    检测CRC32是否匹配
    """
    if binascii.crc32(txt.encode()) in crcNum:
        print("CRC32 of {} is-> 0x{:02X}".format(txt, binascii.crc32(txt.encode())))

def splicing(txt,num):
    """
    拼接CRC32测试值
    """
    num += 1
    tmp = txt
    for j in range(startASCII,endASCII):
        tmp += chr(j)
        if num == crcLen:
            checkCRC32(tmp)
        else:
            splicing(tmp,num)
        tmp = txt

def main():
    """
    主入口
    """
    for i in range(startASCII, endASCII):
        num = 1
        txt = chr(i)
        splicing(txt, num)
    endTime = time.perf_counter()
    print("用时: %f s" % (endTime - startTime))

if startASCII >= endASCII or startASCII < 0 or endASCII > 127:
    print("请检查代码设置的ASCII码起始值与初始值!")
else:
    main()

