# dict = {'name' : 'Piyush Sharma', 'age' : 25}
# print('Name in Dict is :', dict['name'])
# print('Age in the Dict is :', dict['age'])
# dict.clear()
# print('Using the Clear Method :', dict)
# dict_copied = dict.copy()
# print('Using the Copy Method :', dict_copied)
# key = ('house_name', 'house_no')
# value = ('Bhole Killa', '5')
# dict2 = dict.fromkeys(key, value)
# dict2 = dict.fromkeys(key)
# dict2 = dict.fromkeys(['apple', 'banana', 'kiwi'], 0)
# print('Using the fromkeys Method :', dict2)
# first_value = dict.get('name')
# print('Using the get Method :', first_value)
# items_in_dict = dict.items()
# print('Using the items Method :', items_in_dict)
# keys_in_dict = dict.keys()
# print('Using the keys Method :', keys_in_dict)
# values_in_dict = dict.values()
# print('Using the values Method :', values_in_dict)
# poped_item = dict.pop('name')
# print('Using the popped Method :', poped_item)
# print(dict)
# poped_item = dict.popitem() # last value in the dictinary !
# print('Using the popitem Method :', poped_item)
# dict.setdefault('Gender', None)
# print('Using the setDefault Method :', dict)
# dict.update({'House_no': 5})
# print('Using the update Method :', dict)

# variable_dict = {'name':'Piyush Sharma', 'age':20, 'house_no': 5}
# print(variable_dict)
# ans = [keys for keys in variable_dict]
# print(variable_dict[ans[0]])
# for x in variable_dict:
#     print(variable_dict[x])
# for x in variable_dict.keys():
#     print(x)
# for x in variable_dict.values():
#     print(x)

child1 = {
  "name" : "Piyush",
  "year" : 2004
}
child2 = {
  "name" : "Dhruv",
  "year" : 2007
}
child3 = {
  "name" : "Denuka",
  "year" : 2011
}
myFamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myFamily['child1']['name'])
print(myFamily['child2']['name'])
print(myFamily['child3']['name'])







