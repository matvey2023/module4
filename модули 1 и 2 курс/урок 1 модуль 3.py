# name = input("Введите имя сотрудника: ")
# salary = int(input("Введите имя сотрудника: "))
#
# print(f"У {name} зарплата в год составляет {salary*12} рублей")
#
# employee = {'name': "Иван",
#             'salary' : 100000}
# print(f"У {employee['name']} зарплата в год составляет {employee['salary']*12} рублей")
# print(f"У {employee.get('name')} зарплата в год составляет {employee.get('salary')*12} рублей")
# employee['age']=23
# print(employee)

# employee_list = [
#     {'name':"Иван",
#      'salary': 100_000},
#     {'name':"Данил",
#      'salary':150_000},
#     {'name':"Олег",
#      'salary':200_000}
# ]
# print(employee_list[0])
# print(employee_list[-1])
# for employee in employee_list:
#     if employee["name"]=="Иван":
#         employee_list.remove(employee)
#         break
# new_employee={
#     'name':'Иван',
#     'salary':100_000
# }
# employee_list.append(new_employee)
# for employee in employee_list:
#     print(f"Имя: {employee['name']}, зарплата: {employee['salary']} рублей")
# print("Количество сотрудников:", len(employee_list))
class Employee:
    def __init__(self, name, salary, on_vocation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vocation = on_vocation
        self.is_good_employee = is_good_employee
    def gen_info(self):
        return f"Имя: {self.name}, зарплата: {self.salary} руб."

employees = [
    Employee("Данил", 300000, False, True),
    Employee("Никита", 250000, True, True),
    Employee("Кирилл", 150000, False, True),
    Employee("Василий", 120000, False, True),
    Employee("Степан", 180000, True, False)
]
for Employee in employees:
    if Employee.is_good_employee==False:
        employees.remove(Employee)
        break
for Employee in employees:
    print(Employee.gen_info())