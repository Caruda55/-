import tkinter as tk
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel('Выход', 'Закрыть приложение?'):
        main_window.destroy()
        

def window_1():
    win = tk.Tk()
    win.title('Рсчёт эквивалентного диаметра воздуховода')
    win.geometry('530x300+397+90')
    win['bg'] = '#33ffe6'
    win.resizable(True, True)

    def calculate():
        height = name_2.get()
        width = name.get()

        if len(width) == 0 or len(height) == 0:
            res.insert(0, 'Поля не заполнены!')
            res.delete(0, tk.END)
            res.insert(0, 'Поля не заполнены!')
        elif height.isalpha() or width.isalpha():
            res.insert(0, 'Только цифры!')
            res.delete(0, tk.END)
            res.insert(0, 'Только цифры!')
        else:
            try:
                result = eval(f'2 * {width} * {height} / ({width} + {height})')
                res.insert(0, str(round(result, 1)))
                res.delete(0, tk.END)
                res.insert(0, str(round(result, 1)))
            except TypeError:
                res.insert(0, 'Ошибка ввода')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')
            except SyntaxError:
                res.insert(0, 'Ошибка ввода!')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')

    def clear():
        name.delete(0, tk.END)
        name_2.delete(0, tk.END)
        res.delete(0, tk.END)

    user_text = tk.Label(win, text='Ширина(мм)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text.grid(row=0, column=0, padx=5, pady=14)
    name = tk.Entry(win, font=('Arial', 15), width=15)
    name.grid(row=0, column=1, columnspan=3)

    user_text_2 = tk.Label(win, text='Высота(мм)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text_2.grid(row=1, column=0, padx=5)
    name_2 = tk.Entry(win, font=('Arial', 15), width=15)
    name_2.grid(row=1, column=1, columnspan=3)

    res_txt = tk.Label(win, text='Результат(мм)', font=('Arial', 19, 'bold'), relief=tk.RAISED, padx=5, pady=3, bg='gray')
    res_txt.grid(row=3, column=6, pady=5, padx=5)
    res = tk.Entry(win, font=('Arial', 15), width=10, justify=tk.CENTER)
    res.grid(row=1, column=6, padx=6, sticky='snwe')

    win.grid_rowconfigure(1, minsize=110)

    btn = tk.Button(win, text='Вычислить', bd=5, font=('Arial', 13), command=calculate)
    btn.grid(row=10, column=0, sticky='we', padx=15, pady=2)

    clear_btn = tk.Button(win, text='Удалить', bd=5, font=('Arial', 13), command=clear)
    clear_btn.grid(row=10, column=2, sticky='we', padx=5)


def window_2():
    win = tk.Tk()
    win.title('Рсчёт воздухообмена по теплоизбыткам')
    win.geometry('835x430+450+120')
    win['bg'] = '#33ffe6'
    win.resizable(True, True)

    def calculate():
        q = name.get()
        p = name_2.get()
        c = name_3.get()
        t_ud = name_4.get()
        t_pr = name_5.get()

        if len(q) == 0 or len(p) == 0 or len(c) == 0 or len(t_ud) == 0 or len(t_pr) == 0:
            res.insert(0, 'Поля не заполнены!')
            res.delete(0, tk.END)
            res.insert(0, 'Поля не заполнены!')
        elif q.isalpha() or p.isalpha() or c.isalpha() or t_ud.isalpha() or t_pr.isalpha():
            res.insert(0, 'Только цифры!')
            res.delete(0, tk.END)
            res.insert(0, 'Только цифры!')
        else:
            try:
                result = eval(f'3.6 * {q} / ({p} * {c} * ({t_ud} - {t_pr}))')
                res.insert(0, str(round(result, 1)))
                res.delete(0, tk.END)
                res.insert(0, str(round(result, 1)))
            except ZeroDivisionError:
                res.insert(0, 'Делить на ноль нельзя')
                res.delete(0, tk.END)
                res.insert(0, 'Делить на ноль нельзя')
            except SyntaxError:
                res.insert(0, 'Ошибка ввода!')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')
            except TypeError:
                res.insert(0, 'Ошибка ввода!')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')

    def clear():
        name.delete(0, tk.END)
        name_2.delete(0, tk.END)
        name_3.delete(0, tk.END)
        name_4.delete(0, tk.END)
        name_5.delete(0, tk.END)
        res.delete(0, tk.END)

    user_text = tk.Label(win, text='Теплота в помещении(Вт)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text.grid(row=0, column=0, pady=14, padx=5, sticky='w')
    name = tk.Entry(win, font=('Arial', 15), width=15)
    name.grid(row=0, column=1, padx=10)

    user_text_2 = tk.Label(win, text='Плотность воздуха в помещении(кг/м3)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text_2.grid(row=1, column=0, padx=5, pady=19, sticky='w')
    name_2 = tk.Entry(win, font=('Arial', 15), width=15)
    name_2.grid(row=1, column=1)

    user_text_3 = tk.Label(win, text='Массовая теплоёмкость воздуха кДж/(кг*С)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text_3.grid(row=2, column=0, padx=5, pady=17, sticky='w')
    name_3 = tk.Entry(win, font=('Arial', 15), width=15)
    name_3.grid(row=2, column=1)

    user_text_4 = tk.Label(win, text='Темп-ра воздуха, удаляемого из помещения С', font=('Arial', 13), relief=tk.RAISED, padx=3, pady=5)
    user_text_4.grid(row=3, column=0, padx=5, pady=20, sticky='w')
    name_4 = tk.Entry(win, font=('Arial', 15), width=15)
    name_4.grid(row=3, column=1)

    user_text_5 = tk.Label(win, text='Темп-ра приточного воздуха С', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text_5.grid(row=4, column=0, padx=5, pady=20, sticky='w')
    name_5 = tk.Entry(win, font=('Arial', 15), width=15)
    name_5.grid(row=4, column=1)

    res_txt = tk.Label(win, text='Результат(м3/час)', font=('Arial', 19, 'bold'),
                       relief=tk.RAISED, padx=8, pady=5, bg='gray')
    res_txt.grid(row=2, column=3)
    res = tk.Entry(win, font=('Arial', 15), width=10, justify=tk.CENTER)
    res.grid(row=1, column=3, sticky='snwe', padx=5)

    btn = tk.Button(win, text='Вычислить', bd=5, font=('Arial', 13), command=calculate)
    btn.grid(row=6, column=0, sticky='we', padx=5, pady=20)

    clear_btn = tk.Button(win, text='Удалить', bd=5, font=('Arial', 13), command=clear)
    clear_btn.grid(row=6, column=1, sticky='we', padx=5)


def window_3():
    win = tk.Tk()
    win.title('Расход воздуха в воздуховоде')
    win.geometry('657x300+510+160')
    win['bg'] = '#33ffe6'
    win.resizable(True, True)

    def calculate():
        v_sr = name.get()
        f = name_2.get()
        if len(v_sr) == 0 or len(f) == 0:
            res.insert(0, 'Поля не заполнены!')
            res.delete(0, tk.END)
            res.insert(0, 'Поля не заполнены!')
        elif v_sr.isalpha() or f.isalpha():
            res.insert(0, 'Только цифры!')
            res.delete(0, tk.END)
            res.insert(0, 'Только цифры!')
        else:
            try:
                result = eval(f'{v_sr} * {f} * 3600')
                res.insert(0, str(round(result, 1)))
                res.delete(0, tk.END)
                res.insert(0, str(round(result, 1)))
            except TypeError:
                res.insert(0, 'Ошибка ввода!')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')
            except SyntaxError:
                res.insert(0, 'Ошибка ввода!')
                res.delete(0, tk.END)
                res.insert(0, 'Ошибка ввода!')
    
    def clear():
        name.delete(0, tk.END)
        name_2.delete(0, tk.END)
        res.delete(0, tk.END)

    user_text = tk.Label(win, text='Средняя скорость(м/с)', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text.grid(row=0, column=0, padx=5, pady=14, sticky='w')
    name = tk.Entry(win, font=('Arial', 15), width=15)
    name.grid(row=0, column=1, columnspan=3)

    user_text_2 = tk.Label(win, text='Площадь сечения проёма', font=('Arial', 13), relief=tk.RAISED, pady=5, padx=3)
    user_text_2.grid(row=1, column=0, padx=5, sticky='w')
    name_2 = tk.Entry(win, font=('Arial', 15), width=15)
    name_2.grid(row=1, column=1, columnspan=3)

    res_txt = tk.Label(win, text='Результат(м3/час)', font=('Arial', 19, 'bold'), relief=tk.RAISED, padx=5, pady=3, bg='gray')
    res_txt.grid(row=3, column=6, pady=5, padx=5)
    res = tk.Entry(win, font=('Arial', 15), width=10, justify=tk.CENTER)
    res.grid(row=1, column=6, padx=6, sticky='snwe')

    win.grid_rowconfigure(1, minsize=110)

    btn = tk.Button(win, text='Вычислить', bd=5, font=('Arial', 13), command=calculate)
    btn.grid(row=10, column=0, sticky='we', padx=15, pady=2)

    clear_btn = tk.Button(win, text='Удалить', bd=5, font=('Arial', 13), command=clear)
    clear_btn.grid(row=10, column=2, sticky='we', padx=5)





main_window = tk.Tk()
main_window.protocol('WM_DELETE_WINDOW', on_closing)
main_window.title('E.C.O   1.0')
main_window.geometry('550x270+300+50')
main_window['bg'] = '#33ffe6'
main_window.resizable(True, True)
photo = tk.PhotoImage(file='logog.png')
main_window.iconphoto(True, photo)

main_window.image = tk.PhotoImage(file='main_pic.png')
bg_logo = tk.Label(main_window, image=main_window.image)
bg_logo.grid(row=4, column=4)


main_window_btn = tk.Button(main_window, text='Рсчёт эквивалентного диаметра воздуховода', bd=4,
                            font=('Arial', 13), command=window_1)
main_window_btn.grid(row=1, column=2, padx=5, pady=6, sticky='w')

main_window_btn2 = tk.Button(main_window, text='Рсчёт воздухообмена по теплоизбыткам', bd=4,
                             font=('Arial', 13), command=window_2)
main_window_btn2.grid(row=4, column=2, padx=5, pady=6, sticky='w')

main_window_btn3 = tk.Button(main_window, text='Расход воздуха', bd=4, font=('Arial', 13), command=window_3)
main_window_btn3.grid(row=5, column=2, padx=5, pady=6, sticky='w')


main_window.mainloop()





