name = input()

def normalize(name_string):

    # put your code here
    dictionary = {"é": "e", "ë": "e", "á": "a", "å": "a", "œ": "oe", "æ": "ae"}
    dictionary_keys = dictionary.keys()
    for key in dictionary_keys:
        name_string = name_string.replace(key, dictionary[key])

    return name_string

print(normalize(name))