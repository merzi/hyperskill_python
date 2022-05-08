from string import ascii_lowercase
# put your python code here
double_alphabet = {}

for char in ascii_lowercase:
    double_alphabet.update({char: char * 2})
