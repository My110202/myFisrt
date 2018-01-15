# -*- coding: UTF-8 -*-
# 任何非0和非空（null）值为te,0或者null为false
# 例1.if else基本语法
flag=False
name='mayue'
if name=='wang':    # 判断条件name是否为wang
    flag=True        # 若条件成立，设置条件为真
    print'welcome you'
else:
    print name      # 若条件不成立，输出narume的值

print '--------------------------------------------------'
# 多个条件判断时，用elif
# 例2
num=3
if num==1:
    print'hello'
elif num==2:
    print'wang'
elif num==3:
    print num

print '--------------------------------------------------'
# 例3
num=5
if num>=1 and num<=10:
    print'welcome'
num=11
if num>=1 and num<=10:
    print'good'
else:
    print'the num is not in range'
num =8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print num
else:
    print"undefine"

print '--------------------------------------------------'
# 在同一行的位置上使用if条件判断语句
var=100
if(var==100):print'yes'
print'good'

print '--------------------------------------------------'
# and短路
a=0
b=1
if ( a > 0 ) and ( b / a > 2 ):
    print "yes"
else :
    print "no"

print '--------------------------------------------------'
# 一个简单的条件循环语句实现汉诺塔问题
def my_print(args):
    print args

def move(n, a, b, c):
    my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))

move (3, 'a', 'b', 'c')