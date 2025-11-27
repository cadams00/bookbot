def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    text = text.split()
    count = 0
    for word in text:
        count += 1
    return count

def char_count(text):
    ccdict = {}
    text = text.split()
    for word in text:
        for letter in word:
            if letter.lower() not in ccdict:
                ccdict[letter.lower()] = 1
            else:
                ccdict[letter.lower()] += 1
    return ccdict

def sort_on(items):
    return items["num"]

def sorted_dict(dictionary):
    s_list = []
    for item in dictionary:
        item_dict = {"char": "", "num": 0}
        item_dict["char"] = item
        item_dict["num"] = dictionary[item]
        s_list.append(item_dict)
    s_list.sort(reverse=True,key=sort_on)
    return s_list