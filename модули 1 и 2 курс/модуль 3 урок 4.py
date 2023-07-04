# with open("file3.txt", "w") as f:
#     f.write ("hello, world")
#     print(f.closed)
# print(f.closed)

# import contextlib
# @contextlib.contextmanager
# def str_reverse(my_str):
#     print("Входим в контекстный менеджер")
#     yield my_str [::-1]
#     print("Выходим из контекстного менеджера")
#
# with str_reverse("Hello, world!") as reversed_str:
#     print(f"Выполняем код: {reversed_str}")

# import contextlib
# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print("произошло исключение")
# with exc_handler(IndexError):
#     my_1=[1, 2]
#     print(my_1[3])

def some_func(*args, **kwargs):
    print(f"арги: {args}")
    print(f"кварги: {kwargs}")

# some_func(1, 2, 3, 4)
# some_func(a=1, b=2, c=3, d=4)

some_func(1, 2, 3, 4, a=1, b=2, c=3, d=4)

