# -*- coding: UTF-8 -*-
# 定义函数用def
def printme( str):
   "打印传入的字符串到标准显示设备上"
   print str
   return
# 调用函数
printme('abcde')
printme('这是调用了函数')

a=[1,2,3]   # 属于list类型，a是引用名，没有类型
b="Runoob" # 属于字符型，b是引用名，没有类型
print a,b


print '--------------------------------------------------'
# 传不可变对象
def ChangInt(a):
   a=10
b=2      # b指向int对象2，把2传递给了b,b和a都指向同一个对象，a=10时，新生了一个int对象10,并让a指向他
ChangInt(b)
print b

print '--------------------------------------------------'
# 传可变对象
def changme(mylist):
   mylist.append([1,2,3,4])
   print '函数内取值：',mylist
   return
mylist=[11,22,33,44]
changme(mylist)
print '函数外取值：',mylist

