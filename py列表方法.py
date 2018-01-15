# -*- coding: UTF-8 -*-
# python 方法
# 1.append() 方法用于在列表末尾添加新的对象。
aList = [123, 'xyz', 'zara', 'abc']
aList.append( 2009 )
print "Updated List : ", aList

print '--------------------------------------------------'
# 2.Python List count()方法
bList = [123, 'xyz', 'zara', 'abc', 123]
print "Count for 123 : ", bList.count(123)
print "Count for zara : ", bList.count('zara')

print '--------------------------------------------------'
# 3.extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print "Extended List : ", aList

# 4.Python List index()方法
print '--------------------------------------------------'
aList = [123, 'xyz', 'zara', 'abc']
print "Index for xyz : ", aList.index( 'xyz' )
print "Index for zara : ", aList.index( 'zara' )

print '--------------------------------------------------'
# 5.insert() 函数用于将指定对象插入列表的指定位置
list1=[12,34,78,90]
list1.insert(2,56)      # 2是指定位置，56是指定对象
print list1

print '--------------------------------------------------'
# 6.Python List pop()方法   移除列表中的一个元素（默认为最后一个元素），并且返回该元素的值
aList = [123, 'xyz', 'zara', 'abc','xyz',123]
aList.pop(0)
print aList
# 7.remove() 函数用于移除列表中某个值的第一个匹配项。
aList.remove('xyz')
print aList
# 8.reverse() 函数用于反向列表中元素。对列表元素反向排序   reverse反转
aList.reverse()
print '列表元素反向排序：',aList

print '--------------------------------------------------'
# 9.Python List sort()方法  sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
aList = [123, 'xyz', 'zara', 'abc','xyz',123]
bList = [456,789]
aList.sort()    # sort()无参，对aList排序
print aList
cList = aList + bList
print 'cList:',cList
cList.sort(cmp)
print cList