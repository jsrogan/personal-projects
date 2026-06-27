import json, random


def load_dictionary(filepath):
    with open(filepath, 'r') as merriam:
        data = json.load(merriam)

    return data

#custom function made for getting postion for every word in the dictionary
def map_words(dict_list):
    my_dict = {}
    x = 0
    for entry in dict_list:
        my_dict.update({entry['word']: x})
        x += 1

    return my_dict


def look_up(word):
    word = word.upper()
    words = load_dictionary('dictionary.json')
    positions = map_words(words)

    if word not in positions:
        print('Word not found')
    else:
        print(words[positions[word]])


def word_of_the_day():
    words = load_dictionary('dictionary.json')
    print(random.choice(words))


word_of_the_day()
        


