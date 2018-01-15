# -*- coding: UTF-8 -*-
# python算术运算符
# 加减乘除模运算同C一样 + - * / %     **幂
a=2;b=3
print 'a+b=',a+b
print 'a-b=',a-b
print 'a*b=',a*b
print 'b/a=',b/a            # /除以
print 'b%a=',b%a
print 'a的b次幂为',a**b
print b//a                  # //取整数

print '--------------------------------------------------'
# python比较运算符
# ==等于  !=不等于   <>不等于   >大于    <小于     >=大于等于   <=小于等于  与c语言一样

# python位运算符
# 按位与&  按位或|   按位异或^(相同为0，不同为1)    按位取反~    左移<<    右移>>

# python逻辑运算符
# and布尔与    x and y 如果x为false,返回false，否则返回y的值
# or布尔或     x or y  如果x非0，返回x的值，否则返回y的计算值
# not布尔非

# python成员运算符   Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组
# in 如果在指定的序列中找到相应的值，返回ture
a=7;b=3;c=30
list=[1,2,3,4,5]
if(a in list):
    print'a在列表中'
else:
    print'a不在列表中'
    if(b not in list):
        print'b 不在列表中'
    else:
        print'b 在列表中'
        if(c in list):
            print'c在列表中'
        else:
            print'c不在列表中'

print '--------------------------------------------------'
# python身份运算符
# is    x is y判断两个标识符是否引用同一个对象，引用同一个对象，返回ture
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a=10;b=10
if(a is b):
    print'a和b有相同的标识'
else:
    print'a和b没有相同的标识'

print '--------------------------------------------------'

