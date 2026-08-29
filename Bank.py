import tkinter as tk
from tkinter import Label, Button, Entry, messagebox
import json
import os

FILE_NAME = 'database.json'
balance = 0
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        users_db = json.load(file)
else:
    users_db = {
        'admin': '1234',
        'user': 'qwerty',
        'danil': 'password'
    }
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(users_db, file, ensure_ascii=False, indent=4)

def clic_com():
    root.destroy()
    r2 = tk.Tk()
    r2.title("Login")
    r2.geometry("600x600")
    r2.configure(background="pink")

    label = Label(r2, text='Пожалуйста, введите свой логин и пароль', font=('Arial', 18), bg='purple', fg='white',
                  width=70, height=2)
    label.pack(ipady=30, ipadx=10)

    logi = Entry(r2, bg="white")
    logi.pack(pady=15, ipadx=7)

    passw = Entry(r2, bg="white", show="*")
    passw.pack(ipadx=7)

    def log():
        username = logi.get()
        password = passw.get()
        if username in users_db:
            if users_db[username] == password:
                app(username)
            else:
                title2 = Label(r2, text='Неверный пароль')
                title2.pack()
                r2.after(2100, title2.destroy)
        else:
            title2 = Label(r2, text='Пользователь не найден,зарегестрировать вас?')
            title2.pack(pady=15)
            btn3 = Button(r2, text='Да', font=('Arial', 15), bg='gray', fg='white', width=3)
            btn3.place(rely=0.480, relx=0.4)

            btn4 = Button(r2, text='Нет', font=('Arial', 15), bg='gray', fg='white', width=3)
            btn4.place(rely=0.480, relx=0.5)
            r2.after(6000, title2.destroy)
            r2.after(6000, btn3.destroy)
            r2.after(6000, btn4.destroy)

            def yes():

                users_db[username] = password
                with open(FILE_NAME, 'w', encoding='utf-8') as file:
                    json.dump(users_db, file, ensure_ascii=False, indent=4)
                title2.destroy()
                btn3.destroy()
                btn4.destroy()
                print('Пользователь зарегестрирован')

            def no():
                title2.destroy()
                btn3.destroy()
                btn4.destroy()

            btn3.config(command=yes)
            btn4.config(command=no)

    btn2 = Button(r2, text='Готово', font=('Arial', 15), bg='gray', fg='white', width=15, height=2, command=log)
    btn2.pack(pady=30)

    def app(username):
        r2.destroy()
        appbank = tk.Tk()
        appbank.title("Fake Bank App")
        appbank.geometry("600x600")
        appbank.configure(background="pink")
        apptitl = Label(appbank,text=f'Добро пожаловать, {username}',font=('Arial', 20),bg="purple",fg="white")
        apptitl.pack(ipady=30, ipadx=10)
        balancetitl = Label(text=f'На вашем счету: {balance} Руб',font=('Arial', 17),bg="gray",fg="white")
        balancetitl.pack(ipady=25, ipadx=20)

root = tk.Tk()
root.title("Bank")
root.geometry("600x600")
root.configure(background="pink")

title = Label(root, text="Вас приветствует приложение: 'Fake Bank'!", font=('Arial', 20), bg="purple", fg="black", width=90, height=3)
title.pack(ipady=30, ipadx=10)

btn = Button(root, text="Нажми, чтобы войти", font=('Arial', 16), bg='gray', width=20, height=2, command=clic_com)
btn.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
