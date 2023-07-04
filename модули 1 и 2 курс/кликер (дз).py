import time
from tkinter import *
import random
import emoji

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0
cur_for_b = 0
cur_for_v = 0
def check():
    global points, cur_for_b, cur_for_v
    b.place(x=random.randint(1, 550), y = random.randint(1, 350))
    points += 1
    cur_for_v += 1
    cur_for_b = 0
    label['text'] = points
    # if points == 20:
    #     time.sleep(2)
    #     b['bg'] = 'green'
    if cur_for_v == 10:
        v['text'] = 'ну пожалуйста' + emoji.emojize(":frowning_face:")
    if cur_for_b == 0:
        b['text'] = 'нажми меня'

def check2():
    global points, cur_for_b, cur_for_v
    v.place(x=random.randint(1, 550), y = random.randint(1, 350))
    points += 1
    cur_for_b += 1
    cur_for_v = 0
    label['text'] = points
    # if points == 20:
    #     time.sleep(2)
    #     b['bg'] = 'green'
    if cur_for_b == 10:
        b['text'] = 'ну пожалуйста' + emoji.emojize(":frowning_face:")
    if cur_for_v == 0:
        v['text'] = 'нажми меня'


b = Button(text = 'нажми меня', font = ('Arial', 20), fg = 'black', bg='white', command = check)
b.place(x=200, y=130)
v=Button(text = 'нажми меня', font = ('Arial', 20), fg = 'black', bg='white', command = check2)
v.place(x=300, y=300)
label = Label(text = points, font = ('Arial', 20), fg = 'black')
label.place(x=10, y=10)

window.mainloop()