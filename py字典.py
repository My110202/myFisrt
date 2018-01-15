# -*- coding: UTF-8 -*-
#  items() 函数以列表返回可遍历的(键, 值) 元组数组。
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print "字典值 : %s" % dict.items()
# 遍历字典列表
for key,values in dict.items():
    print key,values

print '--------------------------------------------------'
# update() 函数把字典dict2的键/值对更新到dict里
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print "Value : %s" %  dict

print '--------------------------------------------------'
# pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print pop_obj   # 输出 ：菜鸟教程
print site

print '--------------------------------------------------'
# popitem() 方法随机返回并删除字典中的一对键和值
pop_obj=site.popitem()
print(pop_obj)
print(site)