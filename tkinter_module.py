from tkinter import*
from tkinter import ttk
from datetime import datetime  # for current date and time

dict_student = None
number_of_elements_student = None
length_student = None
interval_student = None
step_student = None


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
        global interval_student
        global step_student

        name_student = name.get()
        date_student = date.get()

        dict_student = dictionary.get()
        number_of_elements_student = number_of_elements.get()
        length_student = length.get()
        interval_student = interval.get()
        step_student = step.get()

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
                      interval_student + '\t' + step_student + '\n')
        results.close()
        window.destroy()

    #  Создание окна
    window = Tk()
    window.attributes('-fullscreen', True)
    window.title('Main information')

    #  Текст Введите имя
    name_text = Label(window, text='Введите имя:')
    name_text.grid(column=0, row=0)
    #  Окошко для ввода имени
    name = Entry(window, width=10)
    name.grid(column=0, row=1)

    #  Текст Введите дату рождения
    date_text = Label(window, text='Введите дату рождения: ')
    date_text.grid(column=0, row=2)
    #  Окошко для ввода даты рождения
    date = Entry(window, width=20)
    date.grid(column=0, row=3)

    #  Текст Выберите словарь
    dictionary_text = Label(window, text='Выберите словарь: ')
    dictionary_text.grid(column=0, row=4)

    #  Выпадающий список со словарями
    dictionary = ttk.Combobox(window,
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

    dictionary.grid(column=0, row=5)
    dictionary.current(0)

    #  Текст кол-во элементов
    num_of_elements = Label(window, text='Введите кол-во уникальных элементов: ')
    num_of_elements.grid(column=0, row=6)
    #  Окошко для ввода кол-ва элементов
    number_of_elements = Entry(window, width=10)
    number_of_elements.grid(column=0, row=7)

    #  Текст введите длину
    length_of_list = Label(window, text='Введите длину последовательности: ')
    length_of_list.grid(column=0, row=8)
    #  Окошко для вводо длины
    length = Entry(window, width=10)
    length.grid(column=0, row=9)

    #  Текст выберите интервал
    interval_text = Label(window, text='Введите временной интервал: ')
    interval_text.grid(column=0, row=10)
    #  Окошка для ввода интервала
    interval = Entry(window, width=10)
    interval.grid(column=0, row=11)

    #  Текст выберите шаг
    step_text = Label(window, text='Выберите шаг N-back: ')
    step_text.grid(column=0, row=12)
    #  Окошка для ввода шага n-back
    step = Entry(window, width=10)
    step.grid(column=0, row=13)

    #  Кнопка для перехода к тесту
    #  Gри нажатии кнопки происходит запись данных в файл и закрытие окна
    next_btn = Button(window, text='Далее', command=get_data)
    next_btn.grid(column=10, row=20)

    window.mainloop()

    return dict_student, number_of_elements_student, length_student, interval_student, step_student
