from tkinter import*
from tkinter import ttk
from datetime import datetime  # for current date and time


dict_student = None
number_of_elements_student = None
length_student = None
interval_student = None
step_student = None

name_student = None
date_student = None


def recoder_for_logical_part(string_to_recode):
    number_of_dictionary = None
    case = 2

    if string_to_recode == "Eng UPPERCASE":
        number_of_dictionary = 2
        case = 1

    if string_to_recode == "Eng lowercase":
        number_of_dictionary = 2
        case = 2

    if string_to_recode == "Rus UPPERCASE":
        number_of_dictionary = 1
        case = 1

    if string_to_recode == "Rus lowercase":
        number_of_dictionary = 1
        case = 2

    if string_to_recode == "Pictures":
        number_of_dictionary = 6

    if string_to_recode == "Numbers":
        number_of_dictionary = 3

    if string_to_recode == 'Figures':
        number_of_dictionary = 4

    if string_to_recode == 'Colors':
        number_of_dictionary = 5

    return number_of_dictionary, case


def recoder_for_logical_part(string_to_recode):
    number_of_dictionary = None
    case = 2

    if string_to_recode == "Eng UPPERCASE":
        number_of_dictionary = 2
        case = 1

    if string_to_recode == "Eng lowercase":
        number_of_dictionary = 2
        case = 2

    if string_to_recode == "Rus UPPERCASE":
        number_of_dictionary = 1
        case = 1

    if string_to_recode == "Rus lowercase":
        number_of_dictionary = 1
        case = 2

    if string_to_recode == "Pictures":
        number_of_dictionary = 6

    if string_to_recode == "Numbers":
        number_of_dictionary = 3

    if string_to_recode == 'Figures':
        number_of_dictionary = 4

    if string_to_recode == 'Colors':
        number_of_dictionary = 5

    return number_of_dictionary, case


def func_window():
    global dict_student
    global number_of_elements_student
    global length_student
    global interval_student
    global step_student

    def get_data():

        global dict_student
        global number_of_elements_student
        global length_student
        # Время к показу
        global interval_student
        # Шаг N-back
        global step_student

        global name_student
        global date_student

        name_student = 'x'
        date_student = 'x'
        var_student = var.get()
        # dict_student = dictionary.get()

        # var_student это номер шаблона, вот все внутри меняй как тебе надо, в файл данные тоже записываются
        # !! еще я поменяла дату в записи файла, но мне каж можно оставить как было до этого
        if var_student == 1:
            number_of_elements_student = '5'
            length_student = '20'
            interval_student = '0.5'
            step_student = '0'
            dict_student = 'Numbers'
        elif var_student == 2:
            number_of_elements_student = '5'
            length_student = '60'
            interval_student = '1'
            step_student = '3'
            dict_student = 'Eng UPPERCASE'
        elif var_student == 3:
            number_of_elements_student = '5'
            length_student = '15'
            interval_student = '1'
            step_student = '1'
            dict_student = 'Pictures'
        else:
            number_of_elements_student = '0'
            length_student = '0'
            interval_student = '0'
            step_student = '0'
            dict_student = 'Figures'

        #  Файл будет называться Имя_ДатаРождения, и при повторном прохождении теста одним человеком, ...
        #  ...данные вписываются в файл этого человека (мне кажется так сравнивать удобнее будет)...
        #  ... + файл записывается в ту же папку, где лежит программа
        log_file = name_student + '_' + date_student + '.txt'
        results = open('.//results//' + log_file, 'a')

        #  Results.write(expInfo['1. Испытуемый:']+'\t'+expInfo['2.
        #  Дата рождения:']+'\t'+expInfo['4. Дата тестирования:']+ '\n')
        results.write(datetime.today().strftime("%Y/%m/%d") + '\t' +
                      dict_student + '\t' + number_of_elements_student + '\t' + length_student + '\t' +
                      interval_student + '\t' + step_student + '\n')
        results.close()
        window.destroy()

    #  Создание окна
    window = Tk()
    height = 720
    width = 1080

    window.geometry('%dx%d' % (width, height))
    window.title('Main information')

    #  Текст Введите имя
    name_text = Label(window, text='Введите имя:')
    name_text.place(relx=.3, rely=.3, anchor='c')
    #  Окошко для ввода имени
    name = Entry(window, width=10)
    name.place(relx=.3, rely=.35, anchor='c')

    #  Текст Введите дату рождения
    date_text = Label(window, text='Введите дату рождения: ')
    date_text.place(relx=.3, rely=.4, anchor='c')
    #  Окошко для ввода даты рождения
    date = Entry(window, width=20)
    date.place(relx=.3, rely=.45, anchor='c')

    # #  Текст Выберите словарь
    # dictionary_text = Label(window, text='Выберите словарь: ')
    # dictionary_text.place(relx=.5, rely=.3, anchor='c')

    # #  Выпадающий список со словарями
    # dictionary = ttk.Combobox(window,
    #                           values=[
    #                               "Eng UPPERCASE",
    #                               "Eng lowercase",
    #                               "Rus UPPERCASE",
    #                               "Rus lowercase",
    #                               "Pictures",
    #                               "Numbers",
    #                               'Figures',
    #                               'Colors'
    #                           ])

    # dictionary.place(relx=.5, rely=.35, anchor='c')
    # dictionary.current(0)

    # #  Текст кол-во элементов
    # num_of_elements = Label(window, text='Введите кол-во элементов: ')
    # num_of_elements.place(relx=.5, rely=.4, anchor='c')
    # #  Окошко для ввода кол-ва элементов
    # number_of_elements = Entry(window, width=10)
    # number_of_elements.place(relx=.5, rely=.45, anchor='c')

    # #  Текст введите длину
    # length_of_list = Label(window, text='Введите длину последовательности: ')
    # length_of_list.place(relx=.5, rely=.5, anchor='c')
    # #  Окошко для вводо длины
    # length = Entry(window, width=10)
    # length.place(relx=.5, rely=.55, anchor='c')

    # #  Текст выберите интервал
    # interval_text = Label(window, text='Введите временной интервал: ')
    # interval_text.place(relx=.5, rely=.6, anchor='c')
    # #  Окошка для ввода интервала
    # interval = Entry(window, width=10)
    # interval.place(relx=.5, rely=.65, anchor='c')

    # #  Текст выберите шаг
    # step_text = Label(window, text='Выберите шаг: ')
    # step_text.place(relx=.5, rely=.7, anchor='c')
    # #  Выпадающий список с шагом
    # step = Entry(window, width=10)
    # step.place(relx=.5, rely=.75, anchor='c')

    #  Текст Шаблон
    date_text = Label(window, text='Шаблон: ')
    date_text.place(relx=.6, rely=.3, anchor='c')

    # сами радиокнопки
    # изменить подпись к шаблону можно в поле текст
    var = IntVar()
    rbutton1 = Radiobutton(window, text='1', variable=var, value=1)
    rbutton2 = Radiobutton(window, text='2', variable=var, value=2)
    rbutton3 = Radiobutton(window, text='3', variable=var, value=3)
    rbutton1.place(relx=.6, rely=.35, anchor='c')
    rbutton2.place(relx=.6, rely=.4, anchor='c')
    rbutton3.place(relx=.6, rely=.45, anchor='c')

    #  Кнопка для перехода к тесту
    #  Gри нажатии кнопки происходит запись данных в файл и закрытие окна
    next_btn = Button(window, text='Далее', padx='20', pady='8', command=get_data)
    next_btn.place(relx=.5, rely=.9, anchor='c')

    window.mainloop()

    return dict_student, number_of_elements_student, length_student, interval_student, step_student, \
           name_student, date_student