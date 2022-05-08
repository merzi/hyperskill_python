import re

# write your code here
player_icons = ["X",
                "O"]
empty_cell_icon = "_"
results = ["Game not finished",
           "Draw",
           f"{player_icons[0]} wins",
           f"{player_icons[1]} wins",
           "Impossible",
           "Error"]


def check_winning_tuples(cells):
    possible_tuples = [[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8],
                       [0, 3, 6],
                       [1, 4, 7],
                       [2, 5, 8],
                       [0, 4, 8],
                       [2, 4, 6]]

    result = False
    for tuple_ in possible_tuples:
        b = 0
        for position in tuple_:
            if position in cells:
                b += 1
        if b == 3:
            result = True
            break

    return result


def normalize_coordinates(coordinate):
    if re.match(r"\d+[,]{1}[\s]{1}\d+", coordinate):
        return coordinate

    if coordinate.find(","):
        coordinate = coordinate.replace(",", " ")

    if re.match(r"[\s]{2,}", coordinate):
        coordinate = re.sub(r"[\s]{2,}", " ", coordinate)

    return ", ".join(coordinate.strip().split(" "))


def coordinate_only_numbers(coordinate):
    ret = True
    for value in coordinate.replace(",", "").replace(" ", ""):
        if re.match(r"\d", value) is not True:
            ret = False

    return ret


def coordinate_in_grid(coordinate):
    ret = False
    coordinate = normalize_coordinates(coordinate)
    for key, value in get_playground_dictionary().items():
        if value == coordinate:
            ret = True

    return ret


def is_coordinate(coordinate_or_number):
    if re.match(r"\d+,?\s+\d+", coordinate_or_number):
        return True
    return False


def create_playground():
    pg = []
    for _ in get_playground_dictionary():
        pg.append("")
    return pg


def fill_cells(cell_list, pg=None):
    if pg is None:
        pg = create_playground()
    for (cell, value) in enumerate(cell_list):
        set_cell_content(pg, cell, value)

    return pg


def set_cell_content(pg, cell_number, content):
    pg[cell_number] = content


def is_cell_empty(pg, cell):
    if is_coordinate(cell):
        cell = coordinate_to_cell_number(cell)

    if pg[cell].strip() == "" or pg[cell].strip() == "_":
        return True
    return False


def get_playground_dictionary():
    return {0: "1, 1",
            1: "1, 2",
            2: "1, 3",
            3: "2, 1",
            4: "2, 2",
            5: "2, 3",
            6: "3, 1",
            7: "3, 2",
            8: "3, 3"}


def cell_number_to_coordinate(number):
    return get_playground_dictionary()[number]


def coordinate_to_cell_number(coordinate):
    number = -1
    coordinate = normalize_coordinates(coordinate)
    for key, cell in get_playground_dictionary().items():
        if cell == coordinate:
            number = key
            break

    return number


def print_table(cell_dictionary):
    print("---------")
    print("| " + cell_dictionary[0] + " " + cell_dictionary[1] + " " + cell_dictionary[2] + " |")
    print("| " + cell_dictionary[3] + " " + cell_dictionary[4] + " " + cell_dictionary[5] + " |")
    print("| " + cell_dictionary[6] + " " + cell_dictionary[7] + " " + cell_dictionary[8] + " |")
    print("---------")


def count_user_cells(cell_dictionary, user_sign):
    return [cell for (cell, value) in enumerate(cell_dictionary) if value.lower() == user_sign.lower()]


def count_empty_cells(cell_dictionary):
    return [cell for (cell, value) in enumerate(cell_dictionary) if value == ' ' or value == '_']


def evaluate_game(pg, player1, player2):
    empty_cells = count_empty_cells(pg)
    player1_cells = count_user_cells(pg, player1)
    player2_cells = count_user_cells(pg, player2)

    player1_win = check_winning_tuples(player1_cells)
    player2_win = check_winning_tuples(player2_cells)

    if player1_win and player2_win or abs(len(player1_cells) - len(player2_cells)) > 1:  # Impossible to solve
        result = 4
    elif player1_win and player2_win is False:  # Player 1 Win
        result = 2
    elif player2_win and player1_win is False:  # Player 2 Win
        result = 3
    elif len(empty_cells) == 0:  # Draw
        result = 1
    elif len(empty_cells) > 0:  # Game not finished
        result = 0
    else:  # Error / unknown game state
        result = 5

    return result


def print_game_result(result, result_strings):
    print(result_strings[result])


def make_move(pg):
    move = None
    while move is None:
        move = input("Enter the coordinate: ")
        if len(move) < 3:
            print("Coorinates should contains 2 numbers!")
            print("\033[F\033[F")
            move = None
        elif is_cell_empty(pg, move) is False:
            print("This cell is occupied! Choose another one!")
            move = None
        elif coordinate_only_numbers(move):
            print("You should enter numbers!")
            move = None
        elif coordinate_in_grid(move) is False:
            print("Coordinates should be from 1 to 3!")
            move = None
    return move


def change_current_player(active_player):
    if active_player == 0:
        return 1
    return 0


def start_game(icons, empty_cell, result_strings):
    playground = fill_cells([empty_cell for _ in range(len(get_playground_dictionary()))])
    current_player = 0
    while True:
        game_state = evaluate_game(playground, icons[0], icons[1])
        if game_state != 0:
            print_game_result(game_state, result_strings)
            break

        set_cell_content(playground,
                         coordinate_to_cell_number(make_move(playground)),
                         icons[current_player])

        print_table(playground)
        current_player = change_current_player(current_player)


start_game(player_icons, empty_cell_icon, results)
