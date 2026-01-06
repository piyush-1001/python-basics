# myList = [1, 20, 30, 1, 4, 5]
# print('The Original List is :', myList)
# myList.append(45)
# print('Appended the  value 45', myList)
# # print('Cleared the List', myList)
# # myList.clear()
# newList = myList.copy()
# print('Copied the List', newList)
# print('Count Function', myList.count(1))
# myList.extend([11, 21, 31, 51, 41])
# print('Extended List', myList)
# print('Index Method Example', myList.index(1, 1))
# myList.insert(1, 2)
# print('Insert Function', myList)
# print('Pop Function last value', myList.pop())
# myList.remove(30)
# print('Remove Function value 30', myList)
# myList.reverse()
# print('Reverse Function', myList)
# myList.sort()
# print('Sorted List', myList)
from future.types import newlist

#
# LIST_1 = [1, 2, 3]
# LIST_2 = [4, 5, 6]
# ans_1 = 4 in LIST_2
# print(ans_1)
# ans_1 = 2 in LIST_2
# print(ans_1)
# ans_2 = 1 not in LIST_2
# print(ans_2)
# ans_2 = 5 not in LIST_2
# print(ans_2)


l = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6]
# l.append(l2)
# print(l)
# l.remove(1)
# print(l)
# l.pop(1)
# print(l)
# l.clear()
# print(l)
# del l
# print(l)
# for no in range(len(l)):
#     print(l[no])
# no = 0
# while no < len(l):
#     print(l[no])
#     no += 1

# [print(x) for x in l]

# fruits = ['apple', 'banana', 'cherry']
# newList = []
# [newList.append(x) for x in fruits if 'a' in x]
# print(newList)
#
# newList = [x for x in fruits if 'apple' not in x]
# print(newList)

# ------------------------------------------------------------------------------ # newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in range(101) if x % 2 == 0]
# print(newlist)
#
# animals = ['tiger', 'lion', 'elephant', 'mouse', 'COW']
# good_list = [animal.upper() for animal in animals]
# print(good_list)

# newAnimals = [x if x != 'tiger' else 'hathi' for x in animals]
# print(newAnimals)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)







