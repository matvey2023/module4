def calc(num_1, num_2, operation):
    if operation == "сложить":
        result = num_1 + num_2
        print("Сумма равна: ", result)
    elif operation == "вычесть":
        result = num_1 - num_2
        print("Разность равна: ", result)
    elif operation == "умножить":
        result = num_1 * num_2
        print("Произведение равно: ", result)
    elif operation == "разделить":
        result = num_1 / num_2
        print("Частное равно: ", result)
    else:
        print("я не знаю такую операцию")
    f=open("results of calculator.txt", "w", encoding='utf-8')
    f.write(str(result))
    return result
num_1 = int(input("Введите 1 число: "))
num_2 = int(input("Введите 2 число: "))
operation=input("Что нужно сделать? Сложить/Вычесть/Умножить/Разделить: ")
operation=operation.lower()
print(calc(num_1, num_2, operation))
