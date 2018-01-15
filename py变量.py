# -*- coding: UTF-8 -*-
#  变量赋值
counter=100 #赋值整型
mile=245.0 #浮点型
name='mayue' #字符型
print counter
print mile
print name

print '--------------------------------------------------'
# 多个变量赋值
# 1.Python允许你同时为多个变量赋值
a=b=c=9
print a,b,c
# 2.也可以为多个对象指定多个变量
i,j,k=1,2,'wang'
print i,j,k

print '--------------------------------------------------'
# 标准数据类型
'''Numbers(数字) String(字符串) List(列表)'''
"""Tuple(元组，数组) Dictionary(字典)"""

# python数字
var1=1
var2=10
print var1,var2

print '--------------------------------------------------'
# python字符串 由数字、字母、下划线组成的一串字符。
str="hello word "
print str
print str[0]    #输出字符串的第一个字符
print str[2:5]  #输出字符串的第三个字符串到第五个
print str[2:]   #从第三个字符开始输出
print str *2    #字符串输出两次
print str+"ok"

print '--------------------------------------------------'
# python列表
list=['wang','gang',520,'ma','yue',1224]
tinylist=['love','you']
print list
print list[1:2]
print list[2:]
print list +tinylist
print tinylist *2

print '--------------------------------------------------'
# Python元组 元组是另一个数据类型，类似于List（列表）
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('wang','gang',520,'ma','yue',1224)
tinytuple=('love','you')
print tuple
print tuple[0:2]
print tuple[2:]
print tuple +tinytuple
print tinytuple *2

print '--------------------------------------------------'
# python字典用{}，由索引（key）键和值（）value组成
dict ={}
dict['one'] ='This is one'
dict[2] ='This is two'
dict[3] ='three'
tinydict={'name':'john','code':1234,'age':20}
print dict['one']      #输出键为'one'的值
print dict[2]           #输出键为2的值
print dict[3]
print tinydict          #输出完整的字典
print tinydict.keys()   #输出字典的键
print tinydict.values() #输出字典的值

print '--------------------------------------------------'
# 变量赋值
a=1;b='god'
# 字符串赋值
str='this is string 1'
# 列表串赋值
list =['this','is','list',2]
# 元组赋值
tuple=('this','is','tuple',3)
# 字典赋值
dict ={1:'this',2:'is',3:'dictionary',4:4}
print a,b
print str
print list
print tuple
print dict
print dict.keys()
print dict.values()



