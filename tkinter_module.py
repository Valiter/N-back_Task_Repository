from tkinter import*
from tkinter import ttk
from datetime import datetime  # for current date and time


def func_win():

    def get_data():
        name_student = Name.get()
        date_student = Date.get()
        dict_student = Dictionary.get()
        number_of_elements_student = Number_of_elements.get()
        length_student = Length.get()
        interval_student = Interval.get()
        step_student = Step.get()

        #  Это(Строки 15-18 и 26) можно убрать, я просто попробовала без использования словаря записывать данные в файл
        #  expInfo = {'1. Испытуемый:':Name_student, '2. Дата рождения:':Date_student}
        #  expInfo['4. Дата тестирования:'] = str(datetime.date(datetime.now()))  # add the current time
        #  FileName = expInfo['1. Испытуемый:']+'_'+expInfo['4. Дата тестирования:']
        #  LogFile = FileName + '.txt'

        #  Файл будет называться Имя_ДатаРождения, и при повторном прохождении теста одним человеком, ...
        #  ...данные вписываются в файл этого человека (мне кажется так сравнивать удобнее будет)...
        #  ... + файл записывается в ту же папку, где лежит программа
        log_file = name_student + '_' + date_student + '.txt'
        results = open(log_file, 'a')
        results.write('Испытуемый\tДата рождения\tДата тестирования\tСловарь\tКол-во лементов\tДлина\tИнтервал\tШаг\n')
        #  По сути строчку сверху можно убрать, она просто показывает какие данные хранятся в файле

        #  Results.write(expInfo['1. Испытуемый:']+'\t'+expInfo['2.
        #  Дата рождения:']+'\t'+expInfo['4. Дата тестирования:']+ '\n')
        results.write(name_student + '\t' + date_student + '\t' + str(datetime.date(datetime.now())) + '\t' +
                      dict_student + '\t' + number_of_elements_student + '\t' + length_student + '\t' +
                      interval_student + '\t' + step_student)
        results.close()
        window.destroy()

    #  Создание окна
    window = Tk()
    window.geometry('1080x720')
    window.title('Main information')

    #  Текст Введите имя
    name_text = Label(window, text='Введите имя:')
    name_text.grid(column=0, row=0)
    #  Окошко для ввода имени
    Name = Entry(window, width=10)
    Name.grid(column=0, row=1)

    #  Текст Введите дату рождения
    date_text = Label(window, text='Введите дату рождения: ')
    date_text.grid(column=0, row=2)
    #  Окошко для ввода даты рождения
    Date = Entry(window, width=20)
    Date.grid(column=0, row=3)

    #  Текст Выберите словарь
    dictionary_text = Label(window, text='Выберите словарь: ')
    dictionary_text.grid(column=0, row=4)

    #  Выпадающий список со словарями
    Dictionary = ttk.Combobox(window,
                              values=[
                                        "Eng UPPERCASE",
                                        "Eng lowercase",
                                        "Rus UPPERCASE",
                                        "Rus lowercase",
                                        "Pictures",
                                        "Numbers",
                                        'Figures',
                                        'Colors'
                              ])

    print(dict(Dictionary))
    Dictionary.grid(column=0, row=5)
    Dictionary.current(0)

    #  Текст кол-во элементов
    num_of_elements = Label(window, text='Введите кол-во элементов: ')
    num_of_elements.grid(column=0, row=6)
    #  Окошко для ввода кол-ва элементов
    Number_of_elements = Entry(window, width=10)
    Number_of_elements.grid(column=0, row=7)

    #  Текст введите длину
    length_of_list = Label(window, text='Введите длину последовательности: ')
    length_of_list.grid(column=0, row=8)
    #  Окошко для вводо длины
    Length = Entry(window, width=10)
    Length.grid(column=0, row=9)

    #  Текст выберите интервал
    interval_text = Label(window, text='Введите интервал: ')
    interval_text.grid(column=0, row=10)
    #  Окошка для ввода интервала
    Interval = Entry(window, width=10)
    Interval.grid(column=0, row=11)

    #  Текст выберите шаг
    step_text = Label(window, text='Выберите шаг: ')
    step_text.grid(column=0, row=12)
    #  Выпадающий список с шагом
    Step = ttk.Combobox(window,
                        values=[
                                        "1-back(11)",
                                        "2-back(101)",
                                        "3-back(1001)",
                        ])

    print(dict(Step))
    Step.grid(column=0, row=13)
    Step.current(0)

    #  Кнопка для перехода к тесту
    #  Gри нажатии кнопки происходит запись данных в файл и закрытие окна
    Next_btn = Button(window, text='Далее', command=get_data)
    Next_btn.grid(column=10, row=20)

    window.mainloop()


func_win()
