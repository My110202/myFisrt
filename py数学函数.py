# -*- coding: UTF-8 -*-
print '--------------------------------------------------'
# 类型转换
print float('10')
print complex(2, 4)
print str(9)
print repr('list')  # 转换成表达式字符串
print tuple('s')  # 转换成元组
print list('a')  # 转换成列表
print chr(97)  # 数字转换成字符
print unichr(67)  # unicode统一码
print ord('a')  # 字符转换成整数值
print hex(12)  # 转换成十六进制
print oct(5)  # 转换成八进制

print '--------------------------------------------------'
# 数学函数
import math
print math.ceil(3.1)          # 返回数字的上入数字
print math.floor(3.9)         # 返回数字的下舍取整
print math.exp(3)             # 3的指数
print cmp(3,2)                # 比较函数cmp(x,y) 若x<y有，取-1，x==y 取0，x>y取1
print math.log(math.e)
print math.log(8,2)           # 以2为底
print math.log10(100)         # 以10为底
print math.modf(-10.5)        # 方法返回x的小数部分与整数部分，两部分的数值符号与x相同，整数部分以浮点型表示
print math.pow(2,3)           # 2的3次方


