# Write your code here
import random

attempts = 8


def welcome():
    print("H A N G M A N")


def menu():
    valid_options = ["play", "results", "exit"]
    msg = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
    r = None
    while r == None:
        r = input(msg)
        if r.lower() not in valid_options:
            print("unknown menu option!")
            r = None
    return r.lower()


def show_results(wins, losts):
    print(f"You won: {wins} times")
    print(f"You lost: {losts} times")


def get_word_list():
    return ("python",
            "java",
            "swift",
            "javascript")


def char_lower_english(char):
    return char.islower() and char.isalpha()


def hide_chars(word, showed_chars_count=0):
    new_word = ""
    if showed_chars_count > 0:
        new_word = word[0:showed_chars_count]
    for _ in range(len(word) - len(new_word)):
        new_word += "-"

    return new_word


def uncover_char(hidden_word, word, char):
    word_list = list(hidden_word)
    for i in range(len(hidden_word)):
        if word[i] == char:
            word_list[i] = char

    return "".join(word_list)


def dice_word(word_list):
    random.seed()
    return random.randint(0, len(word_list) - 1)


def guess_word(guess, word):
    if guess.lower() == word.lower():
        print("You survived!")
    else:
        print("You lost!")
    return guess.lower() == word.lower()


def ask_for_word(max_attempts):
    word = get_word_list()[dice_word(get_word_list())]
    char_set = set(word)
    tried_chars = set()
    masked_word = hide_chars(word)
    attempt = 0
    while attempt < max_attempts:
        attempt_char = input(f"\n{masked_word}\nInput a letter:")
        if len(attempt_char) != 1:
            print("Please, input a single letter.")
         #   attempt += 1
        elif not char_lower_english(attempt_char):
            print("Please, enter a lowercase letter from the English alphabet.")
         #   attempt += 1
        elif attempt_char in tried_chars:
            print("You've already guessed this letter.")
         #   print("No improvements.")
         #   attempt += 1
        elif attempt_char in char_set:
            tried_chars.add(attempt_char)
            masked_word = uncover_char(masked_word, word, attempt_char)
        else:
            tried_chars.add(attempt_char)
            print("That letter doesn't appear in the word.")
            attempt += 1
        if masked_word.count("-") < 1:
            print(f"\n{masked_word}\nYou guessed the word {masked_word}!")
            break

    return guess_word(masked_word, word)


def start_game(tries):
    running = True
    wins = 0
    lost = 0
    welcome()

    while running:
        option = menu()

        if option == "play":
            if ask_for_word(tries):
                wins += 1
            else:
                lost += 1
        elif option == "results":
            show_results(wins, lost)
        elif option == "exit":
            running = False
        else:
            print("unknown menu option")


start_game(attempts)
