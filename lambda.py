import functools

from more_itertools.more import permutation_index

# lambda_value = lambda a, b, c: a + b - c
# print('Used the Lambda Function :', lambda_value(1, 20, 3))

# list_numbers = [1, 2, 3, 4, 5]
# map_func = list(map(lambda x: x * 2, list_numbers))
# print(map_func)

# list_numbers = [1, 2, 3, 4, 5]
# filter_func = list(filter(lambda x: x % 2 != 0, list_numbers))
# print(filter_func)

# list_numbers = [1, 2, 3, 4, 5]
# reduce_func = functools.reduce(lambda x, y: x + y, list_numbers)
# print(reduce_func)

# students = [('Piyush', 20), ('Dhruv', 18), ('Denuka', 22)]
# sorted_studnets = sorted(students, key = lambda x: x[0][1])
# print(sorted_studnets)

# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# print(fact(5))

# def fs(n):
#     if n <= 1:
#         return n
#     else:
#         return fs(n-1) + fs(n-2)
# print(fs(7))

# import sys
# print(sys.getrecursionlimit())
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# def gen():
#     yield 1
#     yield 2
# for value in gen():
#    print(value)

# def counting(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# for num in counting(10):
#     print(num)

# def large_seq(n):
#     for num in range(n):
#         yield num
# gen = large_seq(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def simple_seq():
#     yield 'Piyush'
#     yield 'Dhruv'
#     yield 'Denuka'
# gen = simple_seq()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# list_comp = [x * x for x in range(5)]
# print(list_comp)
#
# gen_comp = (x * x for x in range(5))
# # print(gen_comp)
# print(list(gen_comp))
#
# total = sum(x * x for x in range(10))
# print(total)

# def echo_gen():
#     while True:
#         received = yield
#         print('Received :', received)
# gen = echo_gen()
# next(gen)
# gen.send('Hello')
# gen.send('Wold')
# gen.send('Bye')

# def echo_gen():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     finally:
#         print('Generator Closed !')
# gen = echo_gen()
# print(next(gen))
# gen.close()












