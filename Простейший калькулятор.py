import tkinter as tk
from tkinter import messagebox


def clear():
    ent_res.delete(0, tk.END)


def click_summa():
    a = float(ent_value_1.get())
    b = float(ent_value_2.get())
    c = a + b
    clear()
    ent_res.insert(0, str(c))


def click_dec():
    a = float(ent_value_1.get())
    b = float(ent_value_2.get())
    c = a - b
    clear()
    ent_res.insert(0, str(c))


def click_mul():
    a = float(ent_value_1.get())
    b = float(ent_value_2.get())
    c = a * b
    clear()
    ent_res.insert(0, str(c))


def click_div():
    a = float(ent_value_1.get())
    b = float(ent_value_2.get())
    try:
        c = a / b
        clear()
        ent_res.insert(0, str(c))
    except ZeroDivisionError:
        if b == 0:
            messagebox.showinfo('Ошибка!', 'На ноль делить нельзя, повторите ввод.')




window = tk.Tk()
window.title('Простейший калькулятор')
window.rowconfigure(0, minsize=150, weight=1)
window.columnconfigure(1, minsize=150, weight=1)

fr_buttons = tk.Frame(window)
fr_buttons.pack()

label_val_1 = tk.Label(master=fr_buttons, text='Первое число')
label_val_1.grid(row=0, column=0)

label_val_2 = tk.Label(master=fr_buttons, text='Второе число')
label_val_2.grid(row=1, column=0)

label_val_3 = tk.Label(master=fr_buttons, text='Результат')
label_val_3.grid(row=2, column=0)

ent_value_1 = tk.Entry(master=fr_buttons, width=10)
ent_value_1.grid(row=0, column=1, sticky='e')

ent_value_2 = tk.Entry(master=fr_buttons, width=10)
ent_value_2.grid(row=1, column=1, sticky='e')

ent_res = tk.Entry(master=fr_buttons, width=10)
ent_res.grid(row=2, column=1, sticky='e')

btn_summa = tk.Button(fr_buttons, text='Сложение', command=click_summa)
btn_dec = tk.Button(fr_buttons, text='Вычитание', command=click_dec)
btn_mul = tk.Button(fr_buttons, text='Умножение', command=click_mul)
btn_div = tk.Button(fr_buttons, text='Деление', command=click_div)

btn_summa.grid(row=0, column=2, sticky='ew', padx=5, pady=5)
btn_dec.grid(row=1, column=2, sticky='ew', padx=5)
btn_mul.grid(row=0, column=3, sticky='ew', padx=5, pady=5)
btn_div.grid(row=1, column=3, sticky='ew', padx=5)
fr_buttons.grid(row=0, column=0, sticky='ns')

window.mainloop()
