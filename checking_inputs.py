

"""Модуль для проверки вводимой ползователем информации"""


# 1) Проверка на тип словаря
# 2) Проверка на размер буквы, ЕСЛИ тип словаря 'словарь' собственно
# 3) Проверка количества символов, используемых в символьном ряду
# 4) Проверка допустимости значений интервала
# 5) Проверка длинны итогового списка
#       5.1) Сразу скажу, что итоговый список должен генерироваться с помощью запроса...
#            ... времени тестирования и скорости показа стимулов в стимульном ряду.


import generator_git

"""Название функции и объяснение её работы."""


def checking_inputs_func(type_of_symbols_dict, count_of_using_symbols,
                         interval, length_of_fin_list, type_of_letter=2):

    count_of_dictionaries = generator_git.dictionaries()

    if length_of_fin_list < interval:
        return False

    elif type_of_symbols_dict > len(count_of_dictionaries) or type_of_symbols_dict < 1:
        return False

    # Строчка ниже находится на ее месте по той причине, ...
    # Что до нее необходима проверка на длинну и цифру у стимульного списка.
    count_chosen_dictionary = (count_of_dictionaries[type_of_symbols_dict-1])

    # Проверка ниже не защищает от дурака, но хоть немного спасает от опечаток.
    if count_of_using_symbols > len(count_chosen_dictionary):
        return False

    elif type_of_letter > 2 or type_of_letter < 1:
        return False

    else:
        return True
