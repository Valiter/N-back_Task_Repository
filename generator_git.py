import random


def dictionaries():

    rus_list_for_n_back = {
        1: ["А", "а"], 2: ["Б", "б"], 3: ["В", "в"], 4: ["Г", "г"], 5: ["Д", "д"], 6: ["Е", "е"],
        7: ["Ё", "ё"], 8: ["Ж", "ж"], 9: ["З", "з"], 10: ["И", "и"], 11: ["Й", "й"], 12: ["К", "к"],
        13: ["Л", "л"], 14: ["М", "м"], 15: ["Н", "н"], 16: ["О", "о"], 17: ["П", "п"], 18: ["Р", "р"],
        19: ["С", "с"], 20: ["Т", "т"], 21: ["У", "у"], 22: ["Ф", "ф"], 23: ["Х", "х"], 24: ["Ц", "ц"],
        25: ["Ч", "ч"], 26: ["Ш", "ш"], 27: ["Щ", "щ"], 28: ["Ъ", "ъ"], 29: ["Ы", "ы"], 30: ["Ь", "ь"],
        31: ["Э", "э"], 32: ["Ю", "ю"], 33: ["Я", "я"]
    }

    eng_dict_for_n_back = {
        1: ["A", "a"], 2: ["B", "b"], 3: ["C", "c"], 4: ["D", "d"], 5: ["E", "e"], 6: ["F", "f"],
        7: ["G", "g"], 8: ["H", "h"], 9: ["I", "i"], 10: ["J", "j"], 11: ["K", "k"], 12: ["L", "l"],
        13: ["M", "m"], 14: ["N", "n"], 15: ["O", "o"], 16: ["P", "p"], 17: ["Q", "q"], 18: ["R", "r"],
        19: ["S", "s"], 20: ["T", "t"], 21: ["U", "u"], 22: ["V", "v"], 23: ["W", "w"], 24: ["X", "x"],
        25: ["Y", "y"], 26: ["Z", "z"]
    }

    num_list_for_n_back = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    figure_dict_for_n_back = ["triangle", "sphere", "square", "circle", "pyramid", "oval", "prism"]

    color_dict_for_n_back = ["white", "red", "green", "blue", "yellow", "brown", "black", "orange"]

    return rus_list_for_n_back, eng_dict_for_n_back, num_list_for_n_back, figure_dict_for_n_back, color_dict_for_n_back


def choosing_elements(some_list, count_of_stimulus):
    length_of_list = len(some_list)
    random.shuffle(some_list)
    keys = []

    if length_of_list >= count_of_stimulus:
        for element in some_list:
            if some_list.index(element) < count_of_stimulus:
                keys.append(element)
            else:
                some_list.clear()
    else:
        return False

    return list(keys)


def n_back_choosing_stimulus(dict_in, stimulus_in, type_letter):
    needed_keys_dict = []
    needed_keys_list = None
    count_of_stimulus = stimulus_in
    num_of_dict = dict_in
    dictionary_from_func = dictionaries()

    if (int(num_of_dict) < 6) and (int(num_of_dict) > 0):
        num_of_dict = int(num_of_dict) - 1

        if type((dictionary_from_func[int(num_of_dict)])) is list:
            listed_keys = dictionary_from_func[int(num_of_dict)]
            # Функция может вернуть False и тогда программа сляжет.
            needed_keys_list = choosing_elements(listed_keys, count_of_stimulus)

        elif type((dictionary_from_func[int(num_of_dict)])) is dict:
            keys_from_dict = dictionary_from_func[int(num_of_dict)].keys()

            # Функция может вернуть False и тогда программа сляжет.
            num_to_take_from_dict = choosing_elements(list(keys_from_dict), count_of_stimulus)
            for index in num_to_take_from_dict:
                letter = dictionary_from_func[num_of_dict].get(index)
                needed_keys_dict.append(letter[type_letter - 1])
    else:
        return False

    return needed_keys_dict or needed_keys_list


def mixer_stimulus(line_of_stimulus, num_for_random, line_of_lined_indexes=20):

    def stimulus_index_maker(length, count):
        list_of_stimulus = []
        list_of_stimulus.clear()
        zero = 0

        while zero < length:
            num = random.randint(1, count)
            list_of_stimulus.append(num)
            zero += 1
        else:
            return list_of_stimulus

    indexed_dictionary = {
        1: "", 2: "",
        3: "", 4: "",
        5: "", 6: "",
        7: "", 8: "",
        9: "", 10: ""
    }

    for element in line_of_stimulus:
        index = line_of_stimulus.index(element)
        indexed_dictionary[index + 1] = [element]

    stimulus_index_made = stimulus_index_maker(line_of_lined_indexes, num_for_random)  # Использовать далее!
    end_list = []
    for element in stimulus_index_made:
        end_list.append(indexed_dictionary.get(element)[0])

    return end_list


global_num_of_dict = input("Напишите число от 1-го до 5-ти: ")
global_count_of_stimulus = int(input("Напишите количество символов используемых для создания символьного ряда: "))
# А ведь строчка ниже не нужна, если я не вызываю словарь.
type_of_letter = int(input("Введите размер буквы: 1 - Большая, 2 - Маленькая: "))

length_st = 50
stimulus_fin_list = 20

# Функция может вернуть False и тогда программа сляжет.
chosen_stimulus = n_back_choosing_stimulus(global_num_of_dict, global_count_of_stimulus, type_of_letter)
print(chosen_stimulus)

end_of_thinking = mixer_stimulus(chosen_stimulus, global_count_of_stimulus, int(stimulus_fin_list))
