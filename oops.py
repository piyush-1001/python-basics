# class MyClass:
#     x = 5
# obj_1 = MyClass()
# print('The Value of x in the Class MyClass is :', obj_1.x)
# del obj_1
# print(obj_1)
from encodings.punycode import selective_find
from os import remove


# class Person:
#     def __init__(self, name, age = 10, house_no = 1):
#         self.name = name
#         self.age = age
#         self.house_no = house_no
# person_1 = Person('Piyush', 21, 5)
# print(f'The Name of the Person is {person_1.name}, His Age is {person_1.age}, and his House No is {person_1.house_no}.')
# person_2 = Person('Dhruv')
# print(f'The Name of the Person 2 is {person_2.name}, his age is {person_2.age}, and his House No is {person_2.house_no}.')

# class Demo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#         print(f'This method is for Displaying Details of the Person ....\nThe name of the Person is : {self.name}\nThe Age of the {self.name}  is : {self.age}')
# d_obj = Demo("Hero", 20)
# d_obj.display_info()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def make_name(self):
#         return f'{self.name}'
#     def welcome(self):
#         print(f'Welcoming {self.make_name()}, The Hero !!')
# obj = Person('Piyush Sharma')
# obj.welcome()

# class ModifyClass:
#     def __init__(self, name):
#         self.name = name
# obj = ModifyClass("Piyush")
# print(obj.name)
# obj.name = "Dhruv"
# # del(obj.name)
# print('Changed the name of the Person to :', obj.name)

# class PropertyClassAndObject:
#     gender = 'Male'
#     def __init__(self, name):
#         self.name = name
# obj_1 = PropertyClassAndObject('Piyush')
# obj_2 = PropertyClassAndObject('Dhruv')
# print('The name of the Person is :', obj_1.name)
# print('The name of the Person is :', obj_2.name)
# # print('The Gender of the Person With obj_2 is :', PropertyClassAndObject.gender) # we can also call the Class Property with the Class name as Well !
# print('This is the Class Property :', obj_1.gender)
# print('This is the Class Property :', obj_2.gender)
# PropertyClassAndObject.gender = 'Female'
# print('The Gender of the Person With obj_1 is :', obj_1.gender)
# print('The Gender of the Person With obj_2 is :', obj_2.gender)
# # Adding new Property like age and house_no
# print('---------------- Adding new Properties to the Class -----------------')
# obj_1.age = 20
# print('The Age of the Person With obj_1 is :', obj_1.age)
# obj_2.house_no = 5
# print('The HOuse_no of the Person With obj_2 is :', obj_2.house_no)

# class Calculate:
#     def __init__(self):
#         print("This is the Constructor Method")
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         return a / b
# cal = Calculate()
# print(cal.multiply(2, 3))
# print(cal.divide(12, 6))
# print(int(cal.divide(12, 6)))

# class ExampleStrMethod:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
# p1 = ExampleStrMethod('p1', 1)
# p2 = ExampleStrMethod('p2', 2)
# print(p1)
# print(p2)

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []
#     def add_song(self, song_name):
#         self.songs.append(song_name)
#     def remove_song(self, song_name):
#         self,remove(song_name)
#     def display_songs(self):
#         print(self.songs)
# playlist_1 = Playlist('Sunder')
# playlist_2 = Playlist('Shyam')
# playlist_1.display_songs()
# playlist_1.add_song('Its Done')
# playlist_1.add_song('Bye')
# print('English Songs are Listed Below : ')
# playlist_1.display_songs()
# print()

# del Playlist.display_songs
# playlist_2.display_songs()
# playlist_2.add_song('Ram Aaenge')
# playlist_2.add_song('Hanuma Chalisa')
# print('Hindi Songs are Listed Below : ')
# playlist_2.display_songs()

# class Inheritance:
#     def __init__(self, fname):
#         self.fname = fname
#         print('Super Class Constructor')
#     def display(self):
#         print(self.fname)
# class SubClass(Inheritance):
#     # pass
#     def __init__(self, fname, school):
#         # Inheritance.__init__(self, fname)
#         super().__init__(fname)
#         print('Child Class Constructor')
#         self.fname = fname
#         self.school = school
#     def welcome(self):
#         print('Welcoming', self.fname)
# obj_inheritance = SubClass("Piyush", 'GMCA')
# obj_inheritance.display()
# obj_inheritance.welcome()
# print(obj_inheritance.school)

# class Car:
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print(f'{self.name} has started.')
# class Bike:
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print(f'{self.name} has started.')
# class Boat:
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print(f'{self.name} has started.')
# car_obj = Car('Car')
# car_obj.start()
# bike_obj = Bike('Bike')
# bike_obj.start()
# boat_obj = Boat('Boat')
# boat_obj.start()

# class Vehicle:
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print('Vehicle started.')
# class Car(Vehicle):
#     pass
# class Bike(Vehicle):
#     def start(self):
#         print(f'{self.name} has started.')
#     # pass
# class Boat(Vehicle):
#     def start(self):
#         print(f'{self.name} has started.')
# car_obj = Car('Car')
# bike_obj = Bike('Bike')
# boat_obj = Boat('Boat')
# # car_obj.start()
# # bike_obj.start()
# # boat_obj.start()
# for x in (car_obj, bike_obj, boat_obj):
#     print(x.name)
#     x.start()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def get_private_variable_value(self):
#         print(self.__age)
#     def set_private_variable_value(self, value):
#         self.__age = value
# p1 = Person('Piyush', 20)
# print(p1.name)
# p1.get_private_variable_value()
# p1.set_private_variable_value(30)
# p1.get_private_variable_value()
# print(p1.age)             # ------------------------- Note: Private properties cannot be accessed directly from outside the class. ----------------------------
# print(p1.__age)

# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
# p1 = Person("Piyush", 30000)
# print(p1.name)
# print(p1._salary)            # ---------------------- Note: Protected Variable / Property A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction. ----------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __display(self):
#         print(self.name)
#         print(self.age)
#     def show_details(self):
#         print(self.name)
#         print(self.age)
# p1 = Person("Piyush", 18)
# p2 = Person("Dhruv", 18)
# p1.show_details()
# p2.show_details()
# # p1.__dislpay()
# # p2.__dislpay()                #  Private Method !

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def display(self):
#         print(self.name)
#         print(self.age)
# p1 = Person("John", 25)
# print(p1.name)
# print(p1._Person__age)              # This is how Python mangles the name: print(p1._Person__age) # Not recommended!
# # This is How we can access the Private Variable using the Class name and the Variable NAme itself.
# # _classname__Variable_name (single underscore -> class name -> double underscore -> Variable Name)

# class OuterClass:
#     def __init__(self):
#         self.name = "Outer Class Initiated"
#     class InnerClass:
#         def __init__(self):
#             self.name = "Inner Class Initiated"
#         def display(self):
#             print('This is the Display Method inside the inner Class')
# outer_obj = OuterClass()
# print(outer_obj.name)
# inner_obj = outer_obj.InnerClass()           # Accessing Inner Class from the Outside
# inner_obj.display()

# class Outer:
#     def __init__(self):
#         self.name = 'Piyush'
#     class Inner:
#         def __init__(self, outer):
#             self.outer = outer
#         def show(self):
#             print(self.outer.name)
# outer_obj = Outer()
# inner_obj = outer_obj.Inner(outer_obj)
# inner_obj.show()

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.engine = self.Engine()
#     class Engine:
#         def __init__(self):
#             self.status = ''
#         def start(self):
#             self.status = 'RUNNING'
#             print('Engine started')
#         def stop(self):
#             self.status = 'STOPPED'
#             print('Engine stopped')
#     def drive(self):
#         if self.engine.status == 'RUNNING':
#             print(f'{self.brand} {self.model}')
#         else:
#             print(f'First Start the Engine !')
# car_obj = Car('Mahindra', 'XUV700')
# # car_obj.drive()
# car_obj.engine.start()
# car_obj.drive()

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
    class CPU:
        def process(self):
            print("Processing CPU")
    class RAM:
        def store(self):
            print("Processing RAM")
comp = Computer()
comp.cpu.process()
comp.ram.store()
