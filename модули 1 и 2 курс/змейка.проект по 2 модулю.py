import random
from tkinter import *

window =Tk()
window.title("Змейка")
window.geometry("900x700")
window.resizable(0, 0)

canvas = Canvas(window, width = 900, heigh = 700)
canvas.pack()

class Snake:
    def __init__(self):
        self.x=450
        self.y=350
        self.v=0
        self.photo=PhotoImage(file='змейка.png')
    def up(self, event):
        self.v=-5
    def down(self, event):
        self.v =5
    def right(self, event):
        self.x+=5
    def left(self, event):
        self.x+=-5
    def check_to_eat(self):

class Ball:
    def __init__(self):
        self.x=random.randint(1, 880)
        self.y=self.x+20
    def draw(self):
        canvas.create_oval(self.x, self.x, self.y, self.y, fill='red')

snake=Snake()
ball=Ball()

window.bind('<Key-Up>', snake.up)
window.bind('<Key-Down>', snake.down)
window.bind('<Key-Right>', snake.right)
window.bind('<Key-Left>', snake.left)

window.mainloop()