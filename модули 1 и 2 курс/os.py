import os
#
# current_path = os.path.abspath(__file__)
# print(current_path)
# parent_path = os.path.join(current_path, '..')
# print(parent_path)
#
# def power(a, b):
#     if b==0:
#         return 1
#     if b ==1:
#         return a
#     if b!=1:
#         return a*power(a, b-1)
# print (power(2, 3))


# def factorial(n):
#     if n == 1:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(4))

def get_all_files(path):
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        if os.path.isdir(new_path):
            print('Папка', name)
            get_all_files(new_path)
        else:
            print('    ---', name)

get_all_files(r'D:\Мои документы\Матвей\Python')

