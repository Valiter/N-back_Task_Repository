

"""Тесты"""


import checking_inputs
import generator_git
import analyzer
import tkinter_module


def main_function():
    # Переменная для запуска цикла while.
    switch = True

    """Вызывем интерфейс для ввода данных и работаем с этими данными."""

    list_from_tkinter = tkinter_module.func_window()

    print(list_from_tkinter)

    # Перегоняем выпадающие варианты словарей в численные значения.
    tkinter_reviver = tkinter_module.recoder_for_logical_part(list_from_tkinter[0])
    # Создаем переменные с чиловыми значениями для работы со словарями.
    global_num_of_dict = tkinter_reviver[0]
    type_of_letter = tkinter_reviver[1]

    # Сохраняем введенные значения.
    global_count_of_stimulus = list_from_tkinter[1]
    interval = list_from_tkinter[4]
    stimulus_fin_list = list_from_tkinter[2]

    # Сохраняем время к показу картинки.
    time_to_show_picture = list_from_tkinter[3]

    # Не понимаю почему не работает так,как надо, но со строчкой ниже все работает корректно.
    global_count_of_stimulus = int(global_count_of_stimulus)

    """Цикл для создания рядов, необходимых для видео ряда."""

    chosen_stimulus = None
    end_of_thinking = None
    results_of_true_false = None

    while switch is True:
        if checking_inputs.checking_inputs_func(int(global_num_of_dict), int(global_count_of_stimulus),
                                                int(interval), int(stimulus_fin_list), int(type_of_letter)) is True:

            """Вызовы функций из модуля generator_git.py"""
            # Функция может вернуть False и тогда программа сляжет.
            chosen_stimulus = generator_git.n_back_choosing_stimulus(global_num_of_dict,
                                                                     global_count_of_stimulus,
                                                                     type_of_letter)
            end_of_thinking = generator_git.mixer_stimulus(chosen_stimulus,
                                                           global_count_of_stimulus,
                                                           int(stimulus_fin_list))

            """Вызовы функций из модуля analyzer.py"""
            results_of_true_false = analyzer.working_code_reviev(end_of_thinking, interval)

            """Вывод результатов, для понимания результатов работы программы."""
            print(chosen_stimulus)
            print(end_of_thinking)
            print(results_of_true_false)
            switch = False
            return chosen_stimulus, end_of_thinking, results_of_true_false, time_to_show_picture

        else:
            print("!")
            switch = False

    """Ниже находится передача информации в pygame_module.py."""

    # pygame_module.pict_and_react(time_to_show_picture, end_of_thinking, global_num_of_dict)
