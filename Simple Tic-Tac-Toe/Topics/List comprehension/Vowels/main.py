vowels = 'aeiou'
# create your list here
word = input()

print([char for char in word if vowels.find(char) > -1])
