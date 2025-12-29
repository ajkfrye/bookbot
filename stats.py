def count_words(path):
    with open(path) as file:
        contents = file.read()
        words = contents.split()
        return len(words)


def char_counts(path):
    with open(path) as file:
        contents = file.read()
        lowered = contents.lower()
        unique_chars = set(lowered)
        char_dict = {}
        for char in unique_chars:
            count = lowered.count(char)
            char_dict[char] = count
        return char_dict


def sorted_char_counts(char_dict):
    dict_list = []
    for tup in char_dict.items():
        new_dict = {}
        new_dict["char"] = tup[0]
        new_dict["num"] = tup[1]
        dict_list.append(new_dict)

    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
