import json
from xml.etree.ElementTree import indent

# Serialization
py_object = {"Name":"Piyush", "Age":20}
py_to_json = json.dumps(py_object, indent=10, separators=(' ----- ', ' ===== '))
print(py_to_json)
print(type(py_to_json), '\n')

# Deserialization
# json_value = '{"Name":"Piyush", "Age":20}'
# json_to_py = json.loads(json_value)
# print(json_to_py)
# print(json_to_py['Name'])
# print(type(json_to_py))

# all_types = {
#     'Name':'Piyush',
#     'Age' : 20,
#     'Marks' : [10, 20, 30],
#     'Mobile No.' : (9998522041, 7041978822),
#     'Percentage' : 99.99,
#     'Male' : True,
#     'Female' : False,
# }

# py_to_json = json.dumps(all_types, indent=10)
# print(py_to_json)
# print(type(py_to_json))

# json_types_to_py_obj = '{"name":"Piyush","age":20, "marks" :[10, 20, 30], "Mobile No.":[9998522041, 7041978822], "Percentage":99.99,"Male":true,"Female":false}'
# py_obj = json.loads(json_types_to_py_obj)
# print(py_obj)
# print(type(py_obj['name']))
# print(type(py_obj['age']))
# print(type(py_obj['marks']))
# print(type(tuple(py_obj['Mobile No.'])))
# print(type(py_obj['Percentage']))
# print(type(py_obj['Male']))
# print(type(py_obj['Female']))
