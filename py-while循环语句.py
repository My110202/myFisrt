# -*- coding: UTF-8 -*-
# while循环语句
# eg 1
numbers = [12, 37, 5, 26, 6, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print even
print odd

print '--------------------------------------------------'
# eg 2
count = 5
while (count <= 10):
    print'This is count ', count
    count += 1
print'over,goodbye'

print '--------------------------------------------------'
# eg 3 continue break 用法
i = 1
while i < 10:
    i += 1
    if (i % 2 != 0):
        continue
    else:
        print i

print '--------------------------------------------------'
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

print '--------------------------------------------------'
# break
i = 1
while 1:
    print i
    i += 1
    if (i >= 10):
        break

# 无限循环
print '--------------------------------------------------'
'''var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number  :")
    print "You entered: ", num
print "Good bye!"

print '--------------------------------------------------'
# 简单语句组
flag=1
while(flag):print'given the flag is true'
print"goodbye"'''

print '--------------------------------------------------'
# 循环使用else语句 while … else 在循环条件为 false 时执行 else 语句块：
i = 1
while i < 5:
    print i, 'is less than 5'
    i += 1
else:
    print i, 'is not less than 5'