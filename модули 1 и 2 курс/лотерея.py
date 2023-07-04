 tkinter import *

window = Tk()
window.geometry('1000x500')
window.title('выигрыш')
window.config(bg = 'gray')
window.resizable(width=False, height=False)

def new():

    text_2.place(x=100, y=100)

text = Label(text = 'ВЫ ВЫИГРАЛИ В ЛОТЕРЕЕ!', fg = 'green', bg = 'gray', font=('Courier New', 50))
text.place(x=100, y=100)

text_2 = Label(text = 'Чтобы забрать выигрыш, необходимо внести 1000руб.', fg = 'green', bg = 'gray', font=('Courier New', 20))

b=Button(text = 'Получить выигрыш', font = ('Arial', 24), fg = 'green', bg='black', command = new)
b.place(x=300, y=250)

window.mainloop()