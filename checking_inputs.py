"""Необходим модуль для провери всей поступающей из ввода информации на допустимость к использованию."""
# 1) Проверка на тип словаря
# 2) Проверка на размер буквы, ЕСЛИ тип словаря 'словарь' собственно
# 3) Проверка количества символов, используемых в символьном ряду
# 4) Проверка допустимости значений интервала
# 5) Проверка длинны итогового списка
#       5.1) Сразу скажу, что итоговый список должен генерироваться с помощью запроса...
#            ... времени тестирования и скорости показа стимулов в стимульном ряду.

"""Название функции и объяснение её работы."""


def checking_inputs_func(type_of_symbols_dict, count_of_using_symbols,
                         ability_to_use_interval, length_of_fin_list, type_of_letter=2):
    if length_of_fin_list >= ability_to_use_interval:
        return False

    elif type_of_symbols_dict > 5 or type_of_symbols_dict < 1:
        return False

    #  Проверка ниже не защищает от дурака, но хоть немного спасает от опечаток.
    elif count_of_using_symbols > 33:
        return False

    elif type_of_letter > 2 or type_of_letter < 1:
        return False

    else:
        return True
