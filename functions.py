# def hello():
#     return 'Hello World !'
# print(hello())

# def func(name, /):                  #ONLY positional arguments.
#     print(f'My name is {name}')
# func('Piyush Sharma')

# def my_func(*, name):
#     print(f'My name is {name}')         #only keyword arguments, add *, before the arguments:
# my_func(name = 'Dhruv Sharma')

# Arguments before / are positional-only, and arguments after * are keyword-only:
# def func(a, b, /, *, c, d):
#     print(f'a is {a}\nb is {b}\nc is {c}\nd is {d}')
# func(10, 20, c = 'This is C', d = 456)

# def names(*name):
#     return f'My name is {name[2]}'
# print(names('child3', 'abcd', 'Piyush'))

# def func(greeting, *names):
#     for name in names:
#         print(f'{greeting}{name}')
#     return 1
# func('Hello', ' Piyush', ' Dhruv', ' Denuka')

# def calculate(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(calculate(1, 2, 3, 4))
# print(calculate(1, 4))

# def details(**args):
#     return f'My name is {args['name']} age is {args['age']} house number is : {args['house_no']}'
# print(details(name='Piyush', age=30, house_no=5))

# def func(**args):
#     print(f'My name is {args["name"]} and my age is {args["age"]} and my House Number is {args["house_no"]}')
#     return 1
# func(name = 'Piyush', age = 20, house_no = 5)

# Unpacking Dictionaries with **
# def func(fname, lname):
#     print(f'My fname is {fname} and lname is {lname}')
#     return 1
# person = {'fname': 'Piyush', 'lname': 'Sharma'}
# func(**person)

# def changecase(func):
#     def inner(x):
#         return func(x).title()
#     return inner
# @changecase
# def hello(name):
#     return 'hello,' + name
# print(hello('piyush'))

def changecase(func):
    def inner():
        return func().title()
    return inner
@changecase
def hello():
    return 'hello world'
@changecase
def bye():
    return 'example to see the decorator.'
print(hello())
print(bye())
print('The Actual name of the Function is :', hello.__name__)

# def function_name_is_this():
#     print('Hello world')
# function_name_is_this()
# print('The Name of the Function is :', function_name_is_this.__name__)


