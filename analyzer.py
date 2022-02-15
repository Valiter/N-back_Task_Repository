

"""Модуль для анализа и создания анализированных рядов стимулов."""


"""Функция используется в другой функции.
Функция для анализа индекса проверяемого стимула с индексом, необходимым согласно заранее заданному интервалу."""


def analyzer_n_back(stymulus_line, stimulus_index, interval_to_back):
    if stimulus_index >= interval_to_back + 1:
        index_minus_interval = stimulus_index + 1
        if stymulus_line[index_minus_interval] == stymulus_line[stimulus_index]:
            return True
        else:
            return False
    else:
        return None


"""Функция для создания списка с результатами по совпадениям."""


def working_code_reviev(stimulus_randomised_line, interval_n_back):
    list_of_result = []
    for element in stimulus_randomised_line:
        check = analyzer_n_back(stimulus_randomised_line, stimulus_randomised_line.index[element],interval_n_back)
        list_of_result.append(check)
    return list_of_result
