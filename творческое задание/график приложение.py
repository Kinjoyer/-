from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def approx(vid, x, y, nasvx, nasvy, colr = 'red', errorx = 0, errory = 0):
    x = np.array(x)
    y = np.array(y)
    errorx = np.array(errorx) if errorx else 0
    errory = np.array(errory) if errory else 0
    
    def lin(x, a, b):
        return a*x + b
    def step(x, a):
        return x**a
    def exp(x, a):
        return a**x
    
    if vid == 1:
        popt, pcov = curve_fit(lin, x, y)
        pogr = np.sqrt(np.diag(pcov))
        plt.errorbar(x,y, xerr = errorx, yerr = errory, fmt = '.', color = 'black', label = 'значения')
        plt.plot(x, lin(x, *popt), label = f'линейная аппроксимация {nasvy} = {popt[0]:.2f}*{nasvx}+{popt[1]:.2f}\n погрешность a = {pogr[0]:.2f}\n погрешность b = {pogr[1]:.2f}', color = colr)
    if vid == 2:
        popt, pcov = curve_fit(step, x, y)
        pogr = np.sqrt(np.diag(pcov))
        plt.errorbar(x,y, xerr = errorx, yerr = errory, fmt = '.', color = 'black', label = 'значения')
        plt.plot(x, step(x, *popt), label = f'степенная аппроксимация {nasvy} = {nasvx}^{popt[0]:.2f}\n погрешность a = {pogr[0]:2f}', color = colr)
    if vid == 3:
        popt, pcov = curve_fit(exp, x, y)
        pogr = np.sqrt(np.diag(pcov))
        plt.errorbar(x,y, xerr = errorx, yerr = errory, fmt = '.', color = 'black', label = 'значения')
        plt.plot(x, exp(x, *popt), label = f'показательная аппроксимация {nasvy} = {popt[0]:.2f}^{nasvx}\n погрешность a = {pogr[0]:.2f}', color = colr)
    
    plt.xlabel(nasvx)
    plt.ylabel(nasvy)
    plt.legend()
    plt.grid(True)
    plt.show()

def create_plot():
    nasvx = entry2.get()[0] if len(entry2.get().strip())>0 else 'x'
    nasvy = entry2.get()[2] if len(entry2.get().strip())>0 else 'y'
    colr = clrv.get()

    try:
        x = list(map(float, entry3.get().split()))
        errorx = list(map(float, entry4.get().split())) if entry4.get() else None
        y = list(map(float, entry5.get().split()))
        errory = list(map(float, entry6.get().split())) if entry6.get() else None
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите числовые значения, разделенные пробелом.")
        return

    vid = 1
    if clrv1.get() == 'линейная':
        vid = 1
    elif clrv1.get() == 'степенная':
        vid = 2
    elif clrv1.get() == 'показательная':
        vid = 3
    approx(vid, x, y, nasvx = nasvx, nasvy = nasvy, colr = colr, errorx = errorx, errory = errory)
    
    
root = Tk()
root.title('График')

l1 = Label(text = 'выберите цвет графика')
l1.pack()

clrv = StringVar()
clr = ['red', 'blue', 'green', 'black']
clrcomb = ttk.Combobox(root, textvariable = clrv, values = clr, state = 'readonly')
clrcomb.set('red')
clrcomb.pack()

lt = Label(text = 'выберите тип аппроксимации')
lt.pack()

clrv1 = StringVar()
clr1 = ['линейная', 'степенная', 'показательная']
clrcomb1 = ttk.Combobox(root, textvariable = clrv1, values = clr1, state = 'readonly')
clrcomb1.set('линейная')
clrcomb1.pack()

l2 = Label(text = 'введите названия x и y (необязательно)')
l2.pack()
entry2 = Entry(root)
entry2.pack()

l3 = Label(text = 'введите значения по горизонтали')
l3.pack()
entry3 = Entry(root)
entry3.pack()

l4 = Label(text = 'введите погрешности по горизонтали (необязательно)')
l4.pack()
entry4 = Entry(root)
entry4.pack()

l5 = Label(text = 'введите значения по вертикали')
l5.pack()
entry5 = Entry(root)
entry5.pack()

l6 = Label(text = 'введите погрешности по вертикали (необязательно)')
l6.pack()
entry6 = Entry(root)
entry6.pack()

plot_button = Button(root, text="Создать график", command=create_plot)
plot_button.pack()

root.mainloop()