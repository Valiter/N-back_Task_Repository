

"""Модуль-дополнение к моулю generator.py для анализа и создания анализированных рядов стимулов."""


"""Функция используется в другой функции.
Функция для анализа индекса проверяемого стимула с индексом, необходимым согласно заранее заданному интервалу."""


def analyzer_n_back(stymulus_line, stimulus_index, interval_to_back):
    if stimulus_index >= int(interval_to_back) + 1:
        index_minus_interval = int(interval_to_back) + 1
        if stymulus_line[stimulus_index - index_minus_interval] == stymulus_line[stimulus_index]:
            return True
        else:
            return False
    else:
        return None


"""Функция для создания списка с результатами по совпадениям."""


def working_code_reviev(stimulus_randomised_line, interval_n_back):
    list_of_result = []
    index = 0
    while len(list_of_result) < len(stimulus_randomised_line):
        result = analyzer_n_back(stimulus_randomised_line, index, interval_n_back)
        index += 1
        list_of_result.append(result)
    return list_of_result
