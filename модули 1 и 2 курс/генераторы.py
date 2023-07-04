my_list1 = [x**2 for x in range (1, 1000001)]
print (my_list1)

my_list2 = (x**2 for x in range (1, 1000001))
for elem in my_list2:
    print (elem)
# результаты работы генераторов не умещаются в консоли