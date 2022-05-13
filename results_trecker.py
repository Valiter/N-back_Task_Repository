

"""Анализ данных и перезапись файлов."""


def file_reader(name):

    def rebuildding_lists_function(data):
        list_rlf = []
        for element in data:
            if element == "F":
                list_rlf.append(False)
            elif element == "T":
                list_rlf.append(True)
            elif element == "N":
                list_rlf.append(None)
            else:
                pass

        return list_rlf

    def analyze(ready, reacted):
        res = []
        circle = 0
        ln = len(ready)
        while circle < ln:
            line_1 = rebuildding_lists_function(ready[circle])
            line_2 = rebuildding_lists_function(reacted[circle])
            true_1_count = line_1.count(True)
            true_2_count = line_2.count(True)
            ln_w = len(line_1)

            circle_two = 0
            greats_count = 0
            mistakes_count = 0

            # Тут идет работа со списками на оценку количества T/F
            while circle_two < ln_w:
                if line_1[circle_two] is True:
                    if line_1[circle_two] == line_2[circle_two]:
                        greats_count += 1
                    if line_2[circle_two] is False:
                        mistakes_count += 1
                elif line_1[circle_two] is None:
                    if line_2[circle_two] is True:
                        mistakes_count += 1
                elif line_1[circle_two] is False:
                    if line_1[circle_two] == line_2[circle_two]:
                        pass
                    else:
                        mistakes_count += 1
                else:
                    mistakes_count += 1
                circle_two += 1

            res.append([" | Количество True в списке: " + str(true_1_count)
                        + " | Количество ответов испытуемого: " + str(true_2_count)
                        + " | Количество ошибок: " + str(mistakes_count)
                        + " | Количество совпадений: " + str(greats_count)])
            circle += 1
        return res

    file = open('.//results//' + name + '.txt', 'r')

    readed_from_file = file.readlines()

    length_of_file = len(readed_from_file)
    # Переработанная программой информация на совпадения в ряду
    reworked = readed_from_file[4::6]
    # Реакции испытуемого на ряд
    react = readed_from_file[5::6]

    # Текст результатов, которые мы получили псле обработки.
    results_list = analyze(reworked, react)

    file.close()

    file = open('.//results//' + name + '_reforged.txt', 'w')

    res_count = 0
    start = 6
    while start < length_of_file:
        readed_from_file.pop(start)
        readed_from_file.insert(start, str(results_list[res_count]) + "\n")
        res_count += 1
        start += 6

    file.writelines(readed_from_file)

    file.close()


file_reader(input("Введите название файла: "))
