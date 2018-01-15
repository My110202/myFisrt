# -*- coding: UTF-8 -*-
# Python 元组，元组与列表相似，不同之处在于元组的元素不能修改
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
print 'tpu1=',tup1
print 'tpu2=',tup2
print 'tpu3=',tup3

print '--------------------------------------------------'
# 访问元组,下标法，所以用中括号
print 'tup1[3]',tup1[3]
print 'tup2[1:5]',tup2[1:5]

print '--------------------------------------------------'
# 修改元组，元组的元素不能修改，但是可以对元组进行组合
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
# 以下修改元组元素操作是非法的。
# tup1[0] = 100;
# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;

print '--------------------------------------------------'
# Python 元组 tuple() 函数将列表转换为元组
aList = [123, 'xyz', 'zara', 'abc'];
aTuple = tuple(aList)
print "Tuple elements : ", aTuple


