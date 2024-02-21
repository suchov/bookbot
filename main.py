path_to_file = "books/frankenstein.txt"


def string_count(words):
    my_dict = {}
    lowered_string = words.lower()
    words = lowered_string.split()
    for word in words:
        my_dict[word] = my_dict.get(word, 0) + 1
    return my_dict


def letters_count(letters):
    my_dict = {}
    lowered_string = letters.lower()
    for letter in lowered_string:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    return my_dict


with open(path_to_file) as f:
    file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    print(len(words))
    dic = string_count(file_contents)
    print(dic)
    let_count = letters_count(file_contents)
    print(let_count)
