

""" Основной модуль программы, где используются все остальные элементы для вызова кода."""
import checking_inputs
import generator_git
import analyzer


# Переменная для запуска цикла while.
switch = True


"""Запрашиваемые данные через input()-ы выношу отдельно, чтобы было понятно, что нужно в видео части."""
global_num_of_dict = input("Напишите число от 1-го до 5-ти: ")
global_count_of_stimulus = int(input("Напишите количество символов используемых для создания символьного ряда: "))
# А ведь строчка ниже не нужна, если я не вызываю словарь.
type_of_letter = int(input("Введите размер буквы: 1 - Большая, 2 - Маленькая: "))
interval = input("напишите длинну интервала. 1-back (11), 2-back (101), 3-back (1001).\nНеобходима только цифра шага: ")

"""Тут находятся заранее заданные данные, которые ТОЖЕ надо будет запрашивать или иметь заранее созданные значения."""

stimulus_fin_list = 20

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

    else:
        print("!")
        switch = False
