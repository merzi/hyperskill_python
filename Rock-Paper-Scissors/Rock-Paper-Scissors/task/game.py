# Write your code here
import random
import string


def make_computer_move(possible_choices):
    random.seed()
    return random.choice(possible_choices)


def solve(played_move, possible_choices):
    winning_constellation = {"rock": "scissors",
                             "paper": "rock",
                             "scissors": "paper"}

    loosing_message = string.Template("Sorry, but the computer chose $move")
    draw_message = string.Template("There is a draw ($move)")
    winning_message = string.Template("Well done. The computer chose $move and failed")

    computer_move = make_computer_move(possible_choices)
    if winning_constellation[played_move] == computer_move:
        print(winning_message.substitute(move=computer_move))
        return 100
    elif winning_constellation[computer_move] == played_move:
        print(loosing_message.substitute(move=computer_move))
        return 0

    print(draw_message.substitute(move=computer_move))
    return 50


def read_rating_file(rating_file_path):
    ratings = {}

    try:
        file = open(rating_file_path, "r")
        for line in file.readlines():
            if len(line.strip()) > 0:
                name, points = line.split(" ")
                ratings[name] = int(points)
    except FileNotFoundError:
        print("")
    finally:
        if 'file' in locals():
            file.close()

    return ratings


def write_rating_file(rating_file_path, player_name, points):
    ratings = read_rating_file(rating_file_path)
    ratings[player_name] = points
    try:
        file_opener = open(rating_file_path, "w")
        for name in ratings:
            print(f"{name} {ratings[name]}", end="\n", file=file_opener)

    finally:
        file_opener.close()


def get_player_points(player_name, rating_file):
    ratings = read_rating_file(rating_file)
    return ratings[player_name] if player_name in ratings else 0


def game():
    rating_file = "rating.txt"
    player_name = input("Enter your name:")
    print(f"Hello, {player_name}")
    current_points = get_player_points(player_name, rating_file)
    choices = input()
    if len(choices.strip()) > 0:
        choices = choices.split(",")
    else:
        choices = ["rock", "paper", "scissors"]
    print("Okay, let's start")
    while True:
        move = input()
        if move == "!exit":
            print("Bye!")
            break
        elif move == "!rating":
            print(f"Your rating: {current_points}")
        elif move not in choices:
            print("Invalid input")
        else:
            current_points += solve(move, choices)
            write_rating_file(rating_file, player_name, current_points)


game()
