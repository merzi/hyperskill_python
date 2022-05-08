# Write your code here
import random

player_pieces_count = 7
identical_number_count = 8
stock_size = 28
player1_name = "computer"
player2_name = "player"


def get_new_stock(stock_full_size):
    stock = list()
    full_stock = get_full_stock()
    random.seed()
    while len(stock) < stock_full_size:
        key = random.randint(0, len(full_stock) - 1)
        stock.append(full_stock[key])
        del full_stock[key]

    return stock


def get_full_stock():
    stock = list()
    for num in range(7):
        for num2 in range(7):
            stock.append([num, num2])

    return stock


def give_player_token(pieces_stock, count):
    player_stock = list()
    for n in range(count):
        give_random_token(pieces_stock, player_stock)

    return player_stock


def give_random_token(pieces_stock, snake_player_stock):
    random.seed()
    piece_number = random.randint(0, len(pieces_stock) - 1)
    snake_player_stock.append(pieces_stock[piece_number])
    del pieces_stock[piece_number]


def determine_starting_player(player_1_stock, player_2_stock, domino_snake):
    player1_highest_key = find_highest_pair(player_1_stock)
    player2_highest_key = find_highest_pair(player_2_stock)

    if player1_highest_key == -1 and player2_highest_key == -1:
        return None

    if player1_highest_key == -1:
        domino_snake.append(player_2_stock[player2_highest_key])
        del player_2_stock[player2_highest_key]
        return "2"
    elif player2_highest_key == -1:
        domino_snake.append(player_1_stock[player1_highest_key])
        del player_1_stock[player1_highest_key]
        return "1"
    elif player_1_stock[player1_highest_key][0] > player_2_stock[player2_highest_key][0]:
        domino_snake.append(player_1_stock[player1_highest_key])
        del player_1_stock[player1_highest_key]
        return "1"
    elif player_2_stock[player2_highest_key][0] > player_1_stock[player1_highest_key][0]:
        domino_snake.append(player_2_stock[player2_highest_key])
        del player_2_stock[player2_highest_key]
        return "2"

    return None


def find_highest_pair(player_stock):
    highest_key = -1
    for key in range(len(player_stock)):
        if player_stock[key][0] == player_stock[key][1]:
            if highest_key == -1:
                highest_key = key
            elif player_stock[key][0] > player_stock[highest_key][0]:
                highest_key = key

    return highest_key


def start(pieces, size_of_stock, player_1_name, player_2_name):
    starting_player = None
    stocks = None
    while starting_player is None:
        stocks = shuffle_token(pieces, size_of_stock, player_1_name, player_2_name)
        starting_player = determine_starting_player(stocks[player_1_name],
                                                    stocks[player_2_name], stocks['domino_snake'])
    return starting_player, stocks


def shuffle_token(pieces_count, size_of_stock, player_1_name, player_2_name):
    stock = get_new_stock(size_of_stock)
    player1_pieces = give_player_token(stock, pieces_count)
    player2_pieces = give_player_token(stock, pieces_count)
    domino_snake = list()

    stocks = {'stock': stock,
              player_1_name: player1_pieces,
              player_2_name: player2_pieces,
              'domino_snake': domino_snake}

    return stocks


def place_token(player_stock, token_number, domino_snake, stock):
    if token_number < 0:
        check_token_orientation(player_stock[abs(token_number + 1)], domino_snake[0], True)
        domino_snake.insert(0, player_stock[abs(token_number + 1)])
        del player_stock[abs(token_number + 1)]
    elif token_number > 0:
        check_token_orientation(player_stock[token_number - 1], domino_snake[len(domino_snake) - 1])
        domino_snake.append(player_stock[token_number - 1])
        del player_stock[token_number - 1]
    elif len(stock) > 0:
        random.seed()
        k = random.randint(0, len(stock) - 1)
        player_stock.append(stock[k])
        del stock[k]


def check_token_orientation(player_token, snake_token, at_start=False):
    if at_start and player_token[1] != snake_token[0]:
        player_token.reverse()
    elif at_start is False and player_token[0] != snake_token[1]:
        player_token.reverse()


def print_player_token(player_stock):
    print("Your pieces:")
    for key in range(len(player_stock)):
        print(f"{key + 1}:{player_stock[key]}")
    print()


def print_header(stock, player_1_name, player1_stock, domino_snake):
    print("======================================================================")
    print(f"Stock size: {len(stock)}")
    print(f"{uc_first(player_1_name)} pieces: {len(player1_stock)}")
    snake = "".join(str(entry) for entry in domino_snake)

    if len(domino_snake) > 6:
        snake = ""
        key = 0
        for entry in domino_snake:
            if key < 3:
                snake += str(entry)
            elif key >= len(domino_snake) - 3:
                snake += str(entry)

            if key == 2:
                snake += "..."
            key += 1

    print(f"""
{snake}
    """)


def print_end_screen(stocks, player_1_name, player_2_name, winning_player):
    print_header(stocks['stock'], player_1_name, stocks[player_1_name], stocks['domino_snake'])
    print_player_token(stocks[player_2_name])
    if winning_player is None:
        print("Status: The game is over. It's a draw!")
    elif winning_player == "2":
        print("Status: The game is over. You won!")
    elif winning_player == "1":
        print("Status: The game is over. The computer won!")


def play_round(starting_player, stocks, player_1_name, player_2_name):
    if starting_player == "1":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        try:
            input()
        except KeyboardInterrupt:
            return False

        token = None
        random.seed()
        rates = rate_player_token(stocks[player_1_name], stocks['domino_snake'])
        ignored_keys = []
        while token is None:
            token = highest_rated_key(rates, ignored_keys)
            if token == -1:
                token = 0
                continue

            position = token_can_played(stocks[player_1_name][token], stocks['domino_snake'])
            if position is False:
                ignored_keys.append(token)
                token = None
                continue

            token = (token + 1) * position

        place_token(stocks[player_1_name], token, stocks['domino_snake'], stocks['stock'])
    else:
        print("Status: It's your turn to make a move. Enter your command.")
        key = None
        while key is None:
            try:
                key = int(input())
            except ValueError:
                key = -9999
            except KeyboardInterrupt:
                return False

            if abs(key) > len(stocks[player_2_name]):
                key = None
                print("Invalid input. Please try again.")
                continue

            if not check_play_move(stocks[player_2_name], key, stocks['domino_snake']):
                key = None
                print("Illegal move. Please try again.")
                continue
            elif abs(key) in range(len(stocks[player_2_name]) + 1):
                place_token(stocks[player_2_name], key, stocks['domino_snake'], stocks['stock'])
            else:
                print("Invalid input. Please try again.")
                key = None
                continue

    return True


def highest_rated_key(rates, ignored_keys):
    highest = -1
    for key, value in enumerate(rates):
        if key in ignored_keys:
            continue
        elif highest == -1:
            highest = key
        elif rates[highest] < value:
            highest = key
    return highest


def rate_player_token(player_stock, domino_snake):
    counts = calculate_stock_score(player_stock, domino_snake)
    rates = {}
    for key, value in enumerate(player_stock):
        rates.update({key: rate_token(value, counts)})
    return rates


def rate_token(token, counts):
    rate = counts[token[0]]
    rate += counts[token[1]]
    return rate


def calculate_stock_score(player_stock, domino_snake):
    numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for number in numbers:
        numbers[number] = check_number_stock(player_stock, number)
        numbers[number] += check_number_stock(domino_snake, number)

    return numbers


def check_number_stock(stock, number):
    count = 0
    for entry in stock:
        if entry[0] == number:
            count += 1
        if entry[0] == number:
            count += 1

    return count


def check_play_move(player_stock, played_card_number, domino_snake):
    if abs(played_card_number) > len(player_stock):
        return False

    token = player_stock[abs(played_card_number) - 1]
    if played_card_number == 0:
        return True
    if played_card_number < 0 and number_in_token(domino_snake[0][0], token):
        return True

    return played_card_number > 0 and number_in_token(domino_snake[len(domino_snake) - 1][1], token)


def number_in_token(number, token):
    return number in token


def token_can_played(token, domino_snake):
    if number_in_token(domino_snake[0][0], token):
        return -1
    if number_in_token(domino_snake[len(domino_snake) - 1][1], token):
        return 1
    return False


def determine_game_status(player_1_stock, player_2_stock, domino_snake, identical_num_count, stock):
    check_stack_win(domino_snake, identical_num_count)
    if len(stock) == 0 and check_draw(player_1_stock, player_2_stock, domino_snake) is False:
        return None

    if len(player_1_stock) == 0:
        return "1"
    elif len(player_2_stock) == 0:
        return "2"
    elif check_stack_win(domino_snake, identical_num_count):
        return None

    return 0


def check_draw(player_1_stock, player_2_stock, domino_snake):
    if can_player_make_turn(player_1_stock, domino_snake):
        return True

    if can_player_make_turn(player_2_stock, domino_snake):
        return True

    return False


def can_player_make_turn(player_stock, domino_snake):
    for key in range(len(player_stock) * -1, len(player_stock)):
        if key == 0:
            continue
        if check_play_move(player_stock, key, domino_snake):
            return True
    return False


def check_stack_win(stock, identical_num_count):
    if stock[0][0] == stock[0][1]:
        num_count = 0
        for entry in stock:
            for num in entry:
                if num == stock[0][0]:
                    num_count += 1
        if num_count == identical_num_count:
            return True
    return False


def uc_first(string):
    return string[0].upper() + string[1:]


def game(pieces, player_1_name, player_2_name, size_of_stock, identical_num_count):
    starting_player, stocks = start(pieces, size_of_stock, player_1_name, player_2_name)

    if starting_player == "1":
        current_player = "2"
    else:
        current_player = "1"

    while True:
        print_header(stocks['stock'], player_1_name, stocks[player_1_name], stocks['domino_snake'])
        print_player_token(stocks[player_2_name])
        if play_round(current_player, stocks, player_1_name, player_2_name) is False:
            break

        winning_player = determine_game_status(stocks[player_1_name], stocks[player_2_name],
                                               stocks['domino_snake'], identical_num_count,
                                               stocks['stock'])

        if winning_player != 0:
            print_end_screen(stocks, player_1_name, player_2_name, winning_player)
            break

        if current_player == "1":
            current_player = "2"
        else:
            current_player = "1"


game(player_pieces_count, player1_name, player2_name, stock_size, identical_number_count)
