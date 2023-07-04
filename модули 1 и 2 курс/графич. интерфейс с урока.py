from tkinter import *

window = Tk()
window.geometry('700x500')
window.title('Самый сложный тест по вселенной Marvel')

label_title = Label(text = 'Тестирование по вселенной Marvel',
                    font = ('Arial', 24), fg = 'white', bg = 'red')
label_title.place(width = 700, height = 50, x = 0, y = 0)

facts = [
    {'text' : 'Человеческое имя Халка - Брюс Беннет',
     'right' : 1},
    {'text' : 'Уолт Дисней является создателем вселенной Marvel',
     'right' : 0},
    {'text' : 'До появления костюма супергероя, человек муравей занимался воровством',
     'right' : 1},
    {'text': 'Выдуманный город Дженоша является родиной Черный Пантеры',
     'right' : 0}
]
cur_q = 0
points = 0
def check():
    global cur_q, points
    answer = var.get()
    if answer == facts[cur_q]['right']:
        points += 1
    if cur_q < len(facts)-1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text']
    else:
        points_label = Label(text = 'Вы набрали '+ str(points) + ' очков',
                             font = ('Arial', 24), fg = 'red', bg = 'white')
        points_label.place(x = 0, y = 0, width = 700, height = 250)

fact = Message(text = facts[cur_q]['text'], font = ('Arial', 14), width = 680,
               borderwidth = 0)
fact.configure(justify = CENTER)
fact.place(x=10, y=70)
var = IntVar()
false = Radiobutton(text = 'Ложь', variable = var, value = 0)
false.place(x=10, y=120)
true = Radiobutton(text = 'Правда', variable = var, value = 1)
true.place(x=10, y = 170)
b = Button(text = 'Ответить', font = ('Arial', 24), fg = 'black', command = check)
b.place(x = 200, y = 130)


window.mainloop()

# #Программа-кликер
# from tkinter import *
# import random
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
# points = 0
# def check():
#     global points
#     b.place(x=random.randint(1, 550), y = random.randint(1, 350))
#     points += 1
#     label['text'] = points
#
#
# b = Button(text = 'нажми меня', font = ('Arial', 20), fg = 'black', command = check)
# b.place(x=200, y=130)
# label = Label(text = points, font = ('Arial', 20), fg = 'black')
# label.place(x=10, y=10)
#
# window.mainloop()