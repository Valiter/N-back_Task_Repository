

""" Модуль для создания рандомизированных рядов стимулов."""


import random


"""В Функции ниже находятся списки и словари, содержащие необходимые стимулы для создания стимульного ряда."""


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

    figure_dict_for_n_back = ["triangle_up", "square", "circle", "oval", "prism", "triangle_down"]

    color_dict_for_n_back = ["white", "red", "green", "blue", "yellow", "brown", "black", "orange", "beige"]

    picture_dictionary_for_n_back = ["again", "good", "ura", "enter", "pause", "ball", "ball_face", "ball_on_tree",
                                     "boy_musition", "bucket", "cat", "computer", "cop", "doctor", "duck",
                                     "elza", "family", "fire_quard", "flower_2", "flower",  "fridge", "frog",
                                     "girl_painter", "good", "grandmother", "jam", "jerry", "lion", "man", "mouse",
                                     "blank", "phone", "pig", "popcorn", "pot", "reader", "snake", "sun",
                                     "teacher", "tree", "turtle", "warrior", "watermelon", "driver", "red_car",
                                     "builder"
                                     ]

    return rus_list_for_n_back, eng_dict_for_n_back, num_list_for_n_back, \
        figure_dict_for_n_back, color_dict_for_n_back, picture_dictionary_for_n_back


"""Функция ниже используется в другой функции. Сама функция создает список рандомизированных ключей или элементов, 
которые будут в дальнейшем использовться для создания уже стимульного ряда."""


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


"""Функция ниже использует функцию choosing_elements внутри себя. Сама функция создает список уникальных символов."""


def n_back_choosing_stimulus(dict_in, stimulus_in, type_letter):
    needed_keys_dict = []
    needed_keys_list = None
    count_of_stimulus = stimulus_in
    num_of_dict = dict_in
    dictionary_from_func = dictionaries()
    length = len(dictionaries())

    if (int(num_of_dict) < length + 1) and (int(num_of_dict) > 0):
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


"""Функция создает стимульный ряд необходимой длинны. 
Необходимы выбранные стимулы, количество этих самых символов и длинна стимульного ряда.
На выходе получается псевдорандомный список стимулов."""


def mixer_stimulus(line_of_stimulus, count_of_stimulus, line_of_lined_indexes=20):

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

    stimulus_index_made = stimulus_index_maker(line_of_lined_indexes, count_of_stimulus)
    end_list = []
    for element in stimulus_index_made:
        end_list.append(indexed_dictionary.get(element)[0])

    return end_list
