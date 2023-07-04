# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         self.__age = age
#     def print_info(self):
#         print(f"Имя {self._name}, возраст {self.__age}")
#
# Tom = Person("Tom",12)
# Tom.get_age()
# Tom.print_info()
# Tom.set_age(15)
# print(Tom._name, Tom.get_age())

# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
# s=Singleton()
# print("Object created", s)
# s1=Singleton()
# print("Object created", s1)

# def repair_deco(func):   #название декоратора, аргумент какая-то функция
#     def wrapper(a, b)    #обёртка(сами действия, совершаемые при вызове декоратора
#         return func(a, b) - 1
#     return wrapper
# @repair_deco  # автоматически в качестве аргумента передается след. функция
# def wrong_func(a, b):
#     return a+b+1

# print(wrong_func(2,2))

# from datetime import datetime
#
# def timeit(func):
#     def wrapper(val):
#         start = datetime.now()
#         res = func(val)
#         end=datetime.now()
#         print(f"time:{end - start}")
#         return res
#     return wrapper
# @timeit
# def get_list_1(val):
#     return [x for x in range(val) if x%2]
#
# @timeit
# def get_list_2(val):
#     new_list = []
#     for x in range(val):
#         if x%2:
#             new_list.append(x)
#     return new_list
#
# val = 1000000
# a=get_list_1(val)
# b=get_list_2(val)
