dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']


def check_word(word_dictionary, word):
    return word in word_dictionary


def check_sentence(word_dictionary, sentence):
    return [word for word in sentence.split(" ") if check_word(word_dictionary, word) is False]


incorrect_words = check_sentence(dictionary, input())
if incorrect_words:
    print("\n".join(incorrect_words))
else:
    print("OK")
