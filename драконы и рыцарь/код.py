import random
from tkinter import *

window=Tk()
w=600
h=600
window.geometry(str(w) + 'x' + str(h))

canvas=Canvas(window, width=w, heigh=h)
canvas.place(in_ = window, x=0, y=0)
bg_photo=PhotoImage(file='замок.png')

class Knight:
    def __init__(self):
        self.x=70
        self.y=h//2
        self.v=0
        self.photo=PhotoImage(file='рыцарь картинка.png')
    def up(self, event):
        self.v=-5
    def down(self, event):
        self.v =5
    def stop(self, event):
        self.v =0
    def right(self, event):
        self.x+=10
    def left(self, event):
        self.x+=-10
class Dragon:
    def __init__(self):
        self.x=750
        self.y=random.randint(100,500)
        self.v=random.randint(1,3)
        self.photo = PhotoImage(file='дракон картика.png')

knight=Knight()
dragons=[]
for i in range(3):
    dragons.append(Dragon())
def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    knight.y += knight.v
    canvas.create_image(knight.x, knight.y, image=knight.photo)


    current_dragon=0
    dragon_to_kill= -1
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)
        if ((dragon.x - knight.x)**2) + ((dragon.y-knight.y)**2) <= (96)**2:
            dragon_to_kill=current_dragon
        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text="you lose!", font = "Verdana 42", fill='red')
            break
    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]
    if len(dragons)==0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text = " you win!", font = "Verdana 42", fill='red')
    else:
        window.after(5, game)

game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)


window.mainloop()