# from tkinter import *
#
# window = Tk()
# window.title("Форточка")
# window.geometry('500x500+300+300')
# count=0
# def click():
#     global count
#     count+=1
#     lab['text'] = count
#
# lab = Label(window, text = "Красивый вид на горы", bg = "white", fg = '#500', font='16')
# lab.place(x=100, y=100)
#
# btn=Button(text="Нажми меня", bg='purple', fg='#131313', font='16', command = click)
# btn.place(x=200, y=200)
#
# window.mainloop()
from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window=Tk()
window.geometry("400x300+300+300")
window.title('Курс валют')

today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req' : today}

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params = payload)
xml=BeautifulSoup(responce.content, features="xml")

def get_course(id):
    return xml.find('Valute', {"ID" : id}).Value.text

img = PhotoImage(file="logo.png")
logo = Label(window, image=img)
logo.place(x=0, y=0)

lab = Label(window, text="Курс валют \n Код Будущего", font="Arial 18")
lab.place(x=170, y=20)

course_info = Label(window, text="Курс валют на: "+ today.replace("/", "."), font = "Arial 15")
course_info.place(x=90, y=260)

usd_course = Label(window, text="$ "+get_course("R01235"), font='Arial 16')
usd_course.place(x=100, y=190)

usd_course2 = Label(window, text="€: "+get_course("R01239"), font='Arial 16')
usd_course2.place(x=100, y=220)

window.mainloop()