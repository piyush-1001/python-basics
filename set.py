from termios import VDISCARD

variable_Set = {1, 2, 3, 4, 5}
print("This is the Original Set Variable :", variable_Set)
variable_Set.add(6)
print(f'Add Method is used : {variable_Set}')
variable_Set.update([70, 80, 90])
print(f'Update Method is used : {variable_Set}')
variable_Set.remove(70)
print(f'Remove Method is used : {variable_Set}')
variable_Set.discard(4)
print(f'Discard Method is used : {variable_Set}')
variable_Set.pop()
print(f'Pop Method is used : {variable_Set}')
variable_Set_2 = {101, 102, 103, 2, 5}
variable_Set_3 = {1001, 10202, 1043, 2, 5}
variable_Set_4 = (10001, 10022, 106453, 2, 5)
set_5 = variable_Set.union(variable_Set_2, variable_Set_3, variable_Set_4)
print(f'Union Method is used : {set_5}')
set_5.update(variable_Set_2, variable_Set_3, variable_Set_4)
print(f'Update Method is used : {set_5}')
set_6 = set_5.intersection(variable_Set_2)
print(f'Intersection Method is used : {set_6}')
set_6.intersection_update(set_5)
print(f'Intersection_update Method id used : {set_6}')
set_6 = set_5.difference(variable_Set_2)
print(f'Difference Method id used : {set_6}')
set_6.difference_update(variable_Set_2)
print(f'Difference_update Method id used : {set_6}')
variable_Set.symmetric_difference(variable_Set_2)
print(f'symmetric_difference Method id used : {set_6}')




