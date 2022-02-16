from tkinter import *

""" Создадим окно и зададим размеры с расположением """
wind_screen = Tk()  # root - это Переменная! с помощью которой мы вызываем методы, например title.
wind_screen.title("Графическая программа на Python")  # Заголовок окна.
wind_screen.geometry("720x480")  # Размер окна.
# root.geometry("400x300+300+250") - Начальная позиция окна.
# Изначально идет в левый верхний угол экрана. Только в tkinter!

""" Добавим текст и зададим его размер со стилем """
lbl = Label(wind_screen, text="Привет", font=("Times New Roman",100))
# lbl = Label(window, text="Привет", font=("Arial Bold", 50)
# font= Может передаваться ЛЮБОМУ виджету.
lbl.grid(column=0, row=0)  # если Grid не вызвать, то функция не вызовется.


""" Добавим кнопку """
# btn = Button(wind_screen, text="Не нажимать, иначе я вас покараю!!!")
btn = Button(wind_screen, text="Не нажимать!", bg="blue", fg="red")  # Изменяем цвет bg - задний фон, fg - буквы
btn.grid(column=1, row=0)

wind_screen.mainloop()  # Создается, вроде как, только одно окно.
