word = input()
is_palindrome = True

for key, char in enumerate(word):
    if char == word[len(word) - 1 - key]:
        continue

    is_palindrome = False
    break

print("Palindrome" if is_palindrome else "Not palindrome")
