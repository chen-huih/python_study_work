for i in 'hello':
    print(ord(i))  # ord输出字符的ACILL码的值
list1 = [3, 8, 5, 6, 7]
# print(sorted(list1, reverse=True))
# print(list1)
# list1.sort()
# print(list1)
list2 = [0]*5
list2[2:4] =list1[2:4]
print(list2)
