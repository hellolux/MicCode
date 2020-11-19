# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/19 11:18
# @Function: PNG宽高CRC32爆破测试

import binascii
import struct
import sys

"""
本段为PNG图中的IHDR段的十六进制数据
49 48 44 52 00 00 00 FF 00 00 00 F2 08 02 00 00 00 B1 6A 97 9D
49 48 44 52 : IHDR
00 00 00 FF : width
00 00 00 F2 : height
08 02 00 00 00 : end
B1 6A 97 9D : CRC32
"""

# 输入整段十六进制数据
IHDR = "49 48 44 52 00 00 00 FF 00 00 00 F2 08 02 00 00 00 B1 6A 97 9D"
# 处理空格
IHDR = ''.join(IHDR.split())

# 检测长度是否符合标准
if len(IHDR) != 42:
    print("请检测是否截取完整长度的16进制数据")
    sys.exit()

# 截取出头部
testHead = IHDR[0:8]
if testHead != '49484452':
    print("请检测16进制是否从49 48 44 52开始截取")
    sys.exit()

# 截取出宽度
testWidth = bytes.fromhex(IHDR[8:16])
# 截取出高度
testHeight = bytes.fromhex(IHDR[16:24])
# 截取出尾部
testEnd = bytes.fromhex(IHDR[24:34])
# 截取出CRC32
testCRC32 = int.from_bytes(bytes.fromhex(IHDR[34:42]), byteorder='big')

def check(flag,testKnow,tmpCheck,tmpWord):
    """
    CRC32爆破检测是否修改宽高度
    :param flag: 判断宽度/高度模式，True=求宽度,False=求高度
    :param testKnow: 已知的宽度/高度
    :param tmpCheck: 需要检测的高度/宽度
    :param tmpWord: 打印的字符显示
    """
    for i in range(0, 65535):
        tmp = struct.pack('>i', i)
        if flag: testData = bytes.fromhex(testHead) + tmp + testKnow + testEnd
        else: testData = bytes.fromhex(testHead) + testKnow + tmp + testEnd
        if (binascii.crc32(testData) & 0xffffffff) == testCRC32:
            res = int.from_bytes(tmp, byteorder='big')
            tmpR = "计算得出"+tmpWord+"十六进制为: 0x%08X 十进制为: %s"
            if int.from_bytes(tmpCheck, byteorder='big') == res:
                tmpR += " "+ tmpWord + "无修改"
            else:
                tmpR += " "+ tmpWord + "有修改"
            print(tmpR % (res, res))

# 宽度检测
check(True,testHeight,testWidth,"宽度")
# 高度检测
check(False,testWidth,testHeight,"高度")