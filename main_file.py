
indexed_dictionary = {
    1: "", 2: "",
    3: "", 4: "",
    5: "", 6: "",
    7: "", 8: "",
    9: "", 10: ""
}

list_of_stimulus = [1, 2, 4, 6, 7, "A", "n", 'L']

for element in list_of_stimulus:
    index = list_of_stimulus.index(element)
    indexed_dictionary[index + 1] = [element]
print(indexed_dictionary)
