from tkinter import *

window=Tk()
window.geometry('700x500')
window.title('Тест по сериалу Андор')

label_title=Label(text='Тестирование по сериалу "Андор"',
                  font=('Arial', 24), fg='white', bg='black')
label_title.place(width = 700, height = 50, x=0, y=0)

facts=[
    {'text' : 'Кассиан был рабочим в мастерской на Ферриксе',
     'right' : 0},
    {'text' : 'Андор собирался продать Лютену навигационный модуль Starpath',
     'right' : 1},
    {'text' : 'Ограбление имперской базы на Алдани было организовано Лютеном',
     'right' : 1},
    {'text' : 'Кино умел плавать',
     'right' : 0}
]
cur_q = 0
points = 0

def check():
    global cur_q, points
    answer=var.get()
    if bool(answer) == facts[cur_q]['right']:
        points += 1
    if cur_q < len(facts)-1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text']
    else:
        points_label=Label(text='Вы набрали: ' + str(points) + ' очков.',
                           font = ('Arial', 24), fg='red', bg='white')
        points_label.place(x=0, y=0, width = 700, height = 250)

fact = Message(text = facts[cur_q]['text'], font = ('Arial', 14), width=680, borderwidth=0)
fact.configure(justify=CENTER)
fact.place(x=10, y=70)
var = IntVar()
false = Radiobutton(text='ложь', variable=var, value=0)
false.place(x=10, y=120)
true = Radiobutton(text='правда', variable=var, value = 1)
true.place(x=10, y=170)
b=Button(text = 'Ответить', font = ('Arial', 24), fg='black', command = check)
b.place(x=200, y=130)
cur_q = 0
points = 0




window.mainloop()