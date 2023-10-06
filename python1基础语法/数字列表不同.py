list1 = [2,3,4,5,6]
list2 = [2,3,4,5,7]
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
list3 = list(set1.symmetric_difference(set2))
print(list3)