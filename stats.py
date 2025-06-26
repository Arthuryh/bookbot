def count_words(file):
    words = file.split()
    return len(words)

def sort_on(items):
    return items['num']

def count_characters(file):
    characters = file.lower()
    dictionary = {}

    for ch in characters:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] += 1
    return dictionary

def sort_list(dictionary):
    listed_dictionary = []
    for ch, count in dictionary.items():
        listed_dictionary.append({"name":ch, "num":count})
    listed_dictionary.sort(reverse=True, key=sort_on)
    return listed_dictionary