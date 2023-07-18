import pandas as pd
import csv
from tkinter import Tk
from tkinter import *
# while True:
#     data = pd.read_csv('04UG.csv', encoding='utf-8')
#     print(type(data))
# # print(data.info())
#     d = data['tripduration']
# # print(d)
#     try:
#         h = int(input())
#         for en, var in enumerate(d):
#     # print (type(var))
#             if var == h:
#         # print(en+1)
#                 f = data.iloc[[en+1]]
#                 print(f)
#         if h == 'q':
#             break
#     except:
#         print('ValueError: invalid literal for int() with base 10')
# data = pd.read_excel('abc.xlsx')
def clicked():
    global t
    global f
    t = txt.get()
    # d = data['ID СКУП']
    # for en, var in enumerate(d):
    #     # print(var)
    #     if var == t:
    #         # print(en+1)
    #         f = data.iloc[[en]]['Адрес учреждения']
def clicked2():
    global f
    print("zzz")
    data = pd.read_excel('C:/abc.xlsx')
    d = data['ID СКУП']
    print('xxx')
    print(t)
    for en, var in enumerate(d):
        # print(var)
        if int(var) == int(t):
            print(en+1)
            f = data.iloc[[en]]['Контактный телефон']
            print(f)
            msg = Tk()
            lbl = Label(master=msg, text=int(f), relief=GROOVE)
            lbl.place(x=10, y=10)
            msg.mainloop()
wnd=Tk()
# t=""
f=""
fnt_2 =('Arial', 10, 'bold')
txt=Entry(master=wnd, width=30)
txt.configure(font=fnt_2)
txt.place(x=10,y=50)
btn1=Button(master=wnd,text="okei")
btn1.configure(command=clicked)
btn2=Button(master=wnd,text="start")
btn2.configure(command=clicked2)
btn1.place(x=40,y=80)
btn2.place(x=70,y=80)
# lbl = Label(master=wnd, text='ddddd, '+f+"!", relief=GROOVE)
# lbl.place(x=10,y=10)

wnd.mainloop()

# if f!="":
#     msg=Tk()
#     lbl = Label(master=msg, text='ddddd, '+f+"!", relief=GROOVE)
#     lbl.place(x=10,y=10)
#     msg.mainloop()
# else:
#     wsg=Tk()
#     wsg.title("ssss")
#     wsg.mainloop()
# print(data.info())
# d = data['ID СКУП']
#
# # print("Введите ID СКУП:")
#
# # inp = int(input())
# for en, var in enumerate(d):
#     # print(var)
#     if var == t:
#         # print(en+1)
#         f = data.iloc[[en]]['Контактный телефон']
#         print(f)
#             # if var != inp:
#             #     print("ID СКУП в базе не найден")
#         # if inp == 'q':
#         #     break
#
# # print("ValueError: invalid literal for int() with base 10")
input()
# # print(d)
# # wnd.mainloop()