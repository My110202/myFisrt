# -*- coding: UTF-8 -*-
# 更新列表
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print 'the value of list1[2]:', list1[2]
list1[2] = 1999
print 'the update value of list1[2]:', list1[2]
print list2[1:5]
del list1[1]  # 删除列表元素
print 'the new list1:', list1

print '--------------------------------------------------'
for x in [1, 2, 3]: print x  # 迭代

print '--------------------------------------------------'
# 截取
L = ['Google', 'Runoob', 'Taobao']
print L[2]  # 读取列表中第三个元素
print L[-2]  # 读取列表中倒数第二个元素
print L[1:]  # 从第二个元素开始截取

print '--------------------------------------------------'
# 列表函数&方法   如果 list1 < list2 返回 -1, 如果 list1 == list2 返回 0, 如果 list1 > list2 返回 1
list1, list2 = [123, 'xyz'], [456, 'abc']
print 'list1:', list1
print 'list2', list2
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [786]
print 'list3:', list3
print cmp(list2, list3)

print '--------------------------------------------------'

