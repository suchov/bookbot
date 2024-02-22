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
    words = file_contents.split()
    print(f"--- Begin report of {path_to_file} ---")
    print(len(words), " words found in the document")
    dic = string_count(file_contents)
    # I don't wont to show all the words count - useless for now
    # print(dic)
    let_count = letters_count(file_contents)
    new_dict = {}
    for key, value in let_count.items():
        if key.isalpha():
            new_dict[key] = value
    sorted_dic = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dic.items():
        print(f"The '{key} character was found {value} times")
    # print(let_count)
    print("--- End report ---")
