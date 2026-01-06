myList = [1, 20, 30, 1, 4, 5]
print('The Original List is :', myList)
myList.append(45)
print('Appended the  value 45', myList)
# print('Cleared the List', myList)
# myList.clear()
newList = myList.copy()
print('Copied the List', newList)
print('Count Function', myList.count(1))
myList.extend([11, 21, 31, 51, 41])
print('Extended List', myList)
print('Index Method Example', myList.index(1, 1))
myList.insert(1, 2)
print('Insert Function', myList)
print('Pop Function last value', myList.pop())
myList.remove(30)
print('Remove Function value 30', myList)
myList.reverse()
print('Reverse Function', myList)
myList.sort()
print('Sorted List', myList)








