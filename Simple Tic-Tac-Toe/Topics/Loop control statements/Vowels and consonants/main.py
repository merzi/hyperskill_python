vowels = "aeiou"
alphabetic = "abcdefghijklmnopqrstuvwxyzöäüß"
str_ = input()

for char in str_:
    if char not in alphabetic:
        break
    elif char in vowels:
        print("vowel")
    else:
        print("consonant")
