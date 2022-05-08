# put your python code here
sentence = input().lower().split(" ")
dictionary = {word: sentence.count(word) for word in sentence}

for word, count in dictionary.items():
    print(word, count)
