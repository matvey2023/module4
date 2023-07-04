# # name = input("Введите имя сотрудника: ")
# # salary = int(input("Введите зарплату сотрудника: "))
# #
# # print(f"У {name} зарплата в год составляет {salary*12} руб.")
#
# # employee = {'name' : 'Иван',
# #             'salary' : 100000}
# # print(f"У {employee['name']} зарплата в год составляет {employee['salary']*12} руб.")
# # print(f"У {employee.get('name')} зарплата в год составляет {employee.get('salary')*12} руб.")
# # employee['age'] = 23
# # print(employee)
#
# employee_list = [
#     {
#      'name': 'Иван',
#      'salary': 100_000
#     },
#     {
#      'name': 'Данил',
#      'salary': 150_000
#     },
#     {
#      'name': 'Олег',
#      'salary': 200_000
#     }
# ]
# # print(employee_list[0])
# # print(employee_list[-1])
#
# for employee in employee_list:
#     if employee["name"] == "Иван":
#         employee_list.remove(employee)
#         break
# new_employee = {
#     'name' : 'Кирилл',
#     'salary' : 100_000
# }
# employee_list.append(new_employee)
# for employee in employee_list:
#     print(f"Имя: {employee['name']}, зарплата: {employee['salary']} руб.")
# print("Количество сотрудников:", len(employee_list))

class Employee:    #ctrl + /
    def __init__(self, name, salary, on_vacation):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
    def get_info(self):
        return f"Имя: {self.name}, зарплата: {self.salary} руб."

employees = [
    Employee('Данил', 300_000, False),
    Employee('Никита', 250_000, True),
    Employee('Кирилл', 150_000, False)
]

# for employee in employees:
#     print(f"Имя: {employee.name}, зарплата: {employee.salary} руб.")
for employee in employees:
    print(employee.get_info())