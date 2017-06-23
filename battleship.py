# ---------------------------------------------------------
# IMPORT
import modul
from colorama import init, Fore, Back
import time
import random

# ---------------------------------------------------------
# FUNCTIONS


def display_board():
    print("Player 1 board: \n")
    for i in (range(mult + 1)):
        print(i, end=" ")
    print(" ")
    for row in board:
        print(" ".join(row))

    print("\n" * 2)

    print("Player 2 board: \n")
    for i in (range(mult + 1)):
        print(i, end=" ")
    print(" ")
    for row in board2:
        print(" ".join(row))


def out_of_range():
    print(Fore.YELLOW + "Out of range!" + Fore.WHITE)
    print("")


def ship_placement_row(playerx_row):
    while True:
        def inner_ship_placement_row(playerx_row):
            while True:
                try:
                    if game_mode == "PVP":
                        if playerx_row == "P1ship1_row":
                            P1ship1_row = int(input(Fore.GREEN + "P1 ship1 row: " + Fore.WHITE))
                            return P1ship1_row
                        elif playerx_row == "P1ship2_row":
                            P1ship2_row = int(input(Fore.GREEN + "P1 ship2 row: " + Fore.WHITE))
                            return P1ship2_row
                        elif playerx_row == "P2ship1_row":
                            P2ship1_row = int(input(Fore.CYAN + "P2 ship1 row: " + Fore.WHITE))
                            return P2ship1_row
                        elif playerx_row == "P2ship2_row":
                            P2ship2_row = int(input(Fore.CYAN + "P2 ship2 row: " + Fore.WHITE))
                            return P2ship2_row

                    elif game_mode == "PVC":
                        if playerx_row == "P1ship1_row":
                            P1ship1_row = int(input(Fore.GREEN + "P1 ship1 row: " + Fore.WHITE))
                            return P1ship1_row
                        elif playerx_row == "P1ship2_row":
                            P1ship2_row = int(input(Fore.GREEN + "P1 ship2 row: " + Fore.WHITE))
                            return P1ship2_row
                        elif playerx_row == "P2ship1_row":
                            P2ship1_row = random.randrange(1, mult + 1)
                            time.sleep(0.5)
                            return P2ship1_row
                        elif playerx_row == "P2ship2_row":
                            P2ship2_row = random.randrange(1, mult + 1)
                            time.sleep(0.5)
                            return P2ship2_row
                    else:
                        continue
                except ValueError:
                    print("Please pick a valid input type!\n")
                    continue
        check = inner_ship_placement_row(playerx_row)
        if check > 0 and check < (mult + 1):
            break
        else:
            out_of_range()
    return check


def ship_placement_col(playerx_col):
    while True:
        def inner_ship_placement_col(playerx_col):
            while True:
                try:
                    if game_mode == "PVP":
                        if playerx_col == "P1ship1_col":
                            P1ship1_col = int(input(Fore.GREEN + "P1 ship1 column: " + Fore.WHITE))
                            return P1ship1_col
                        elif playerx_col == "P1ship2_col":
                            P1ship2_col = int(input(Fore.GREEN + "P1 ship2 column: " + Fore.WHITE))
                            return P1ship2_col
                        elif playerx_col == "P2ship1_col":
                            P2ship1_col = int(input(Fore.CYAN + "P2 ship1 column: " + Fore.WHITE))
                            return P2ship1_col
                        elif playerx_col == "P2ship2_col":
                            P2ship2_col = int(input(Fore.CYAN + "P2 ship2 column: " + Fore.WHITE))
                            return P2ship2_col

                    elif game_mode == "PVC":
                        if playerx_col == "P1ship1_col":
                            P1ship1_col = int(input(Fore.GREEN + "P1 ship1 column: " + Fore.WHITE))
                            time.sleep(0.5)
                            return P1ship1_col
                        elif playerx_col == "P1ship2_col":
                            P1ship2_col = int(input(Fore.GREEN + "P1 ship2 column: " + Fore.WHITE))
                            time.sleep(0.5)
                            return P1ship2_col
                        elif playerx_col == "P2ship1_col":
                            P2ship1_col = random.randrange(1, mult + 1)
                            time.sleep(0.5)
                            return P2ship1_col
                        elif playerx_col == "P2ship2_col":
                            P2ship2_col = random.randrange(1, mult + 1)
                            time.sleep(0.5)
                            return P2ship2_col

                    else:
                        continue
                except ValueError:
                    print("Please pick a valid input type!\n")
                    continue
        check = inner_ship_placement_col(playerx_col)
        if check > 0 and check < (mult + 1):
            break
        else:
            out_of_range()
    return check


def same_pos(Px_ship1_row, Px_ship2_row, Px_ship1_col, Px_ship2_col):
    while True:
        if Px_ship1_row == Px_ship2_row and Px_ship1_col == Px_ship2_col:
            print("Ship is already in that position")
            Px_ship2_col = int(input("P1 Ship2 column: "))
            continue
        else:
            break
    return (Px_ship2_col)


def direction():
    if direction_p2 == "v":
        board2[P2ship2_row - 1][P2ship2_col] = "H"
        if P2ship2_row == mult:
            board2[P2ship2_row - 2][P2ship2_col] = "H"
        else:
            board2[P2ship2_row][P2ship2_col] = "H"
    elif direction_p2 == "h":
        board2[P2ship2_row - 1][P2ship2_col] = "H"
        if P2ship2_col == mult:
            board2[P2ship2_row - 1][P2ship2_col - 1] = "H"
        else:
            board2[P2ship2_row - 1][P2ship2_col + 1] = "H"
    else:
        board2[P2ship2_row - 1][P2ship2_col] = "H"
        if P2ship2_col == mult:
            board2[P2ship2_row - 1][P2ship2_col - 1] = "H"
        else:
            board2[P2ship2_row - 1][P2ship2_col + 1] = "H"

# -----------------------------------------------------------
# MAIN

while True:
    modul.titlescreen()

    titlescreen = input("Press S+enter to start the game\n     or Q+enter to quit: ")
    print("\n" * 8)

    if titlescreen == "s" or titlescreen == "S":

        while True:
            game_mode = input(Fore.MAGENTA + "Type 'PVP' for 2player mode or 'PVC' for single player: " + Fore.WHITE)
            if game_mode == "PVP" or game_mode == "PVC":
                break
            else:
                print("Please pick a valid option!")

        while True:
            difficulty = input(Fore.MAGENTA + "Please select difficulty! 1 / 2 / 3 \n" + Fore.WHITE)
            if difficulty == "1" or difficulty == "2" or difficulty == "3":
                break
            else:
                print("Please pick a valid option!")
        time.sleep(1)

        if difficulty == "1":
            mult = 4
        elif difficulty == "2":
            mult = 6
        elif difficulty == "3":
            mult = 8
        #else:
            #continue

        board = []
        board2 = []
        game = 0
        s2 = [False]

        for number in range(1, (mult + 1)):
            board.append([str(number)] + ["o"] * mult)

        for number2 in range(1, (mult + 1)):
            board2.append([str(number2)] + ["o"] * mult)

        display_board()
        print("\n")

# Player 1 ship placement

        P1ship1_row = ship_placement_row("P1ship1_row")

        P1ship1_col = ship_placement_col("P1ship1_col")
        board[P1ship1_row - 1][P1ship1_col] = "h"

        P1ship2_row = ship_placement_row("P1ship2_row")

        P1ship2_col = ship_placement_col("P1ship2_col")
# P1 ship same position check
        P1ship2_col = same_pos(P1ship1_row, P1ship2_row, P1ship1_col, P1ship2_col)
# Direction P1
        direction_p1 = input(Fore.MAGENTA + "Default placement is horizontal, if you wish to place it vertically, please press 'v'! " + Fore.WHITE)
        if direction_p1 == "v":
            board[P1ship2_row - 1][P1ship2_col] = "H"
            if P1ship2_row == mult:
                board[P1ship2_row - 2][P1ship2_col] = "H"
            else:
                board[P1ship2_row][P1ship2_col] = "H"
        elif direction_p1 == "h":
            board[P1ship2_row - 1][P1ship2_col] = "H"
            if P1ship2_col == mult:
                board[P1ship2_row - 1][P1ship2_col - 1] = "H"
            else:
                board[P1ship2_row - 1][P1ship2_col + 1] = "H"
        else:
            board[P1ship2_row - 1][P1ship2_col] = "H"
            if P1ship2_col == mult:
                board[P1ship2_row - 1][P1ship2_col - 1] = "H"
            else:
                board[P1ship2_row - 1][P1ship2_col + 1] = "H"

        print("\n")
        display_board()
        print("\n")

# Player 2 ship placement
        P2ship1_row = ship_placement_row("P2ship1_row")

        P2ship1_col = ship_placement_col("P2ship1_col")
        board2[P2ship1_row - 1][P2ship1_col] = "h"

        P2ship2_row = ship_placement_row("P2ship2_row")

        P2ship2_col = ship_placement_col("P2ship2_col")

# P2 ship same position check
        P2ship2_col = same_pos(P2ship1_row, P2ship2_row, P2ship1_col, P2ship2_col)
# Direction P2
        if game_mode == "PVP":
            direction_p2 = input(Fore.MAGENTA + "Default placement is horizontal, if you wish to place it vertically, please press 'v'! " + Fore.WHITE)
            direction()
        elif game_mode == "PVC":
            random_dir = ["v", "h"]
            time.sleep(0.5)
            direction_p2 = random.choice(random_dir)
            direction()


        print("\n")
        display_board()
        print("\n")

        # PLAYER2 SHIP PLACEMENT end / Game
        while game != 15:

            # Player one  111111111111111111111111111111111111111111111111111111111
            while True:
                try:
                    guess1_row = int(input(Fore.GREEN + "P1 Guess row: " + Fore.WHITE))
                    guess1_col = int(input(Fore.GREEN + "P1 Guess column:" + Fore.WHITE))
                except ValueError:
                    print(Fore.YELLOW + "Invalid input type! Please pick again!\n" + Fore.WHITE)
                    continue
                except TypeError:
                    print(Fore.YELLOW + "Invalid input type! Please pick again!\n" + Fore.WHITE)
                    continue
                if (guess1_row < 1 or guess1_row > mult
                or guess1_col < 1 or guess1_col > mult):
                    print("\n")
                    print(Fore.YELLOW + "Please pick a valid position! \n" + Fore.WHITE)
                    continue

                if board2[guess1_row - 1][guess1_col] == "✖":
                    print("\n")
                    print(Fore.YELLOW + "You hit the ocean there before! Pick another position!" + Fore.WHITE)
                    continue

                elif board2[guess1_row - 1][guess1_col] == "⏺":
                    print("\n")
                    print(Fore.YELLOW + "You hit that ship once! Pick another position!" + Fore.WHITE)
                    guess1_row = int(input(Fore.GREEN + "P1 Guess row: " + Fore.WHITE))
                    guess1_col = int(input(Fore.GREEN + "P1 Guess column:" + Fore.WHITE))
                    continue

                elif (board2[guess1_row - 1][guess1_col] == "H") or (board2[guess1_row - 1][guess1_col] == "h"):
                    board2[guess1_row - 1][guess1_col] = "⏺"
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    a = sum(item.count("H") for item in board2)
                    b = sum(item.count("h") for item in board2)
                    time.sleep(0.5)
                    print(Fore.RED + "P2 ship HIT!" + Fore.WHITE)
                    time.sleep(0.5)
                    if a == 0 and b == 0:
                        print("\n" * 2)
                        display_board()
                        print("\n")
                        print(Fore.RED + "All ships SANK, P1 won!" + Fore.WHITE)
                        time.sleep(0.5)
                        game = 15
                        break
                    break
                elif (board2[guess1_row - 1][guess1_col] == "o"):
                    board2[guess1_row - 1][guess1_col] = "✖"
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print(Fore.GREEN + "Miss!" + Fore.WHITE)
                    time.sleep(0.5)
                    break

# Player two 22222222222222222222222222222222222222222222222222222222222222222

            while True:
                if game == 15:
                    break
                try:
                    if game_mode == "PVP":
                        guess2_row = int(input(Fore.CYAN + "P2 Guess row: " + Fore.WHITE))
                        guess2_col = int(input(Fore.CYAN + "P2 Guess column:" + Fore.WHITE))
                except ValueError:
                    print(Fore.YELLOW + "Invalid input type! Please pick again\n" + Fore.WHITE)
                    continue
                if game_mode == "PVC":
                    time.sleep(0.5)
                    guess2_row = random.randrange(1, mult + 1)
                    guess2_col = random.randrange(1, mult + 1)

                if (guess2_row < 1 or guess2_row > mult
                   or guess2_col < 1 or guess2_col > mult):
                    print("\n")
                    print(Fore.YELLOW + "Please pick a valid position! \n" + Fore.WHITE)
                    continue

                elif board[guess2_row - 1][guess2_col] == "✖":
                    print("\n")
                    print(Fore.YELLOW + "You hit the ocean there before! Pick another position!" + Fore.WHITE)
                    continue

                elif board[guess2_row - 1][guess2_col] == "⏺":
                    print("\n")
                    print(Fore.YELLOW + "You hit that ship once! Pick another position!" + Fore.WHITE)
                    continue
                # HIT
                elif (board[guess2_row - 1][guess2_col] == "H") or (board[guess2_row - 1][guess2_col] == "h"):
                    board[guess2_row - 1][guess2_col] = "⏺"
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    c = sum(item.count("H") for item in board)
                    d = sum(item.count("h") for item in board)
                    print(Fore.RED + "P1 ship HIT!" + Fore.WHITE)
                    time.sleep(0.5)
                    game += 1
                    if c == 0 and d == 0:
                        print("\n" * 2)
                        display_board()
                        print("\n")
                        print(Fore.RED + "All ships SANK, P2 won!" + Fore.WHITE)
                        time.sleep(0.5)
                        game = 15
                        break
                    break
                elif (board[guess2_row - 1][guess2_col] == "o"):
                    board[guess2_row - 1][guess2_col] = "✖"
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print(Fore.CYAN + "Miss!" + Fore.WHITE)
                    time.sleep(0.8)
                    game += 1
                    break

        if game == 15:
            modul.game_over()
            restart = input(Fore.MAGENTA + "Do you want to play one more round?(y or n) " + Fore.WHITE)
            if restart == "y":
                continue
            elif restart == "n":
                break
            else:
                break
    elif titlescreen == "q" or titlescreen == "Q":
        break
