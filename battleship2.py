# ---------------------------------------------------------
# IMPORT
import modul
from colorama import init, Fore, Back

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


def ship_placement_row(player_row):
    while True:
        try:
            if player_row > 0 and player_row < (mult + 1):
                break
            else:
                out_of_range()
                player_row = int(input("P1 ship row: "))
                continue
        except ValueError:
            print("Please insert a number!")
            continue
    return player_row


def ship_placement_col(player_col):
    while True:
        try:
            if player_col > 0 and player_col < (mult + 1):
                break
            else:
                out_of_range()
                player_col = int(input("P1 ship column: "))
                continue
        except ValueError:
            print("Please insert a number!")
            continue
    return player_col


def same_pos(Px_ship1_row, Px_ship2_row, Px_ship1_col, Px_ship2_col):
    while True:
        if Px_ship1_row == Px_ship2_row and Px_ship1_col == Px_ship2_col:
            print("Ship is already in that position")
            Px_ship2_col = int(input("P2 Ship2 column: "))
            continue
        else:
            break
    return (Px_ship2_col)


# -----------------------------------------------------------
# MAIN


rs = [True]
while rs == [True]:
    modul.titlescreen()
    titlescreen = input("Press S+enter to start the game\n     or Q+enter to quit: ")
    print("\n" * 8)

    if titlescreen == "s" or titlescreen == "S":
        difficulty = input("Please select difficulty!")

        if difficulty == "1":
            mult = 4
        elif difficulty == "2":
            mult = 6
        elif difficulty == "3":
            mult = 8

        board = []
        board2 = []
        game = 0
        s = [False]
        s2 = [False]

        for number in range(1, (mult + 1)):
            board.append([str(number)] + ["o"] * mult)

        for number2 in range(1, (mult + 1)):
            board2.append([str(number2)] + ["o"] * mult)

        display_board()
        print("\n")

    # Player 1 ship placement

        P1ship1_row = int(input("P1 Ship1 row: "))
        P1ship1_row = ship_placement_row(P1ship1_row)

        P1ship1_col = int(input("P1 Ship1 column: "))
        P1ship1_col = ship_placement_col(P1ship1_col)
        board[P1ship1_row - 1][P1ship1_col] = "H"

        P1ship2_row = int(input("P1 Ship2 row: "))
        P1ship2_row = ship_placement_row(P1ship2_row)

        P1ship2_col = int(input("P1 Ship2 column: "))
        P1ship2_col = ship_placement_col(P1ship2_col)
        direction = input("Do you want to place your ship vertically or horizontally?(v, h)")
        if direction == "v":
            board[P1ship2_row - 1][P1ship2_col] = "H"
            board[P1ship2_row][P1ship2_col] = "H"
        elif direction == "h":
            board[P1ship2_row - 1][P1ship2_col] = "H"
            board[P1ship2_row - 1][P1ship2_col + 1] = "H"




    # P1 SHIP END / p1 ship same spot
        while True:
            if P1ship1_row == P1ship2_row and P1ship1_col == P1ship2_col:
                print("Ship is already in that position!")
                P1ship2_row = int(input("P1 Ship2 row: "))
                P1ship2_col = int(input("P1 Ship2 column: "))
                continue
            else:
                break

        print("\n")
        display_board()
        print("\n")
    # Player 2 ship placement
        P2ship1_row = int(input("P2 Ship1 row: "))
        P2ship1_row = ship_placement_row(P2ship1_row)

        P2ship1_col = int(input("P2 Ship1 column: "))
        P2ship1_col = ship_placement_col(P2ship1_col)

        P2ship2_row = int(input("P2 Ship2 row: "))
        P2ship2_row = ship_placement_row(P2ship2_row)

        P2ship2_col = int(input("P2 Ship2 column: "))
        P2ship2_col = ship_placement_col(P2ship2_col)
    # P1 SHIP END / p1 ship same spot

        same_pos(P2ship1_row,P2ship2_row, P2ship1_col, P2ship2_col)
        P2ship2_col = same_pos(P2ship1_row,P2ship2_row, P2ship1_col, P2ship2_col)

        """while True:
            if P2ship1_row == P2ship2_row and P2ship1_col == P2ship2_col:
                print("Ship is already in that position")
                P2ship2_row = int(input("P2 Ship2 row: "))
                P2ship2_col = int(input("P2 Ship2 column: "))
                continue
            else:
                break"""

        print("\n")
        # to hide ship position
        display_board()
        print("\n")
    # PLAYER2 SHIP PLACEMENT end / Game
        try:
            while game != 15:

                # player one
                guess1_row = int(input("P1 Guess row: "))
                guess1_col = int(input("P1 Guess column:"))

                # if there is a hit
                while True:
                    if guess1_row == 0 or guess1_col == 0:
                        print("\n")
                        print("Please pick a valid position!")
                        guess1_row = int(input("P1 Guess row: "))
                        guess1_col = int(input("P1 Guess column:"))
                        continue
                    else:
                        break

                while True:
                    try:
                        if board2[guess1_row - 1][guess1_col] == "✖":
                            print("\n")
                            print("You hit the ocean there before! Pick another position!")
                            guess1_row = int(input("P1 Guess row: "))
                            guess1_col = int(input("P1 Guess column:"))
                            continue
                        else:
                            break
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        guess1_row = int(input("P1 Guess row: "))
                        guess1_col = int(input("P1 Guess column:"))
                        continue

                while True:
                    try:
                        if board2[guess1_row - 1][guess1_col] == "⏺":
                            print("\n")
                            print("You hit that ship once! Pick another position!")
                            guess1_row = int(input("P1 Guess row: "))
                            guess1_col = int(input("P1 Guess column:"))
                            continue
                        else:
                            break
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        guess1_row = int(input("P1 Guess row: "))
                        guess1_col = int(input("P1 Guess column:"))
                        continue

                if (s == [True] and guess1_row == P2ship1_row and guess1_col == P2ship1_col or
                s == [True] and guess1_row == P2ship2_row and guess1_col == P2ship2_col):

                    try:
                        board2[guess1_row - 1][guess1_col] = "⏺"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        continue
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print("All ships SANK, P1 won!")
                    game = 15
                    break

                elif (guess1_row == P2ship1_row and guess1_col == P2ship1_col or
                guess1_row == P2ship2_row and guess1_col == P2ship2_col):
                    try:
                        board2[guess1_row - 1][guess1_col] = "⏺"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        continue
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    if s:
                        print("Ship down!")
                    s = [True]

                else:
                    try:
                        board2[guess1_row - 1][guess1_col] = "✖"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        continue
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print("Miss!")

                # player two
                try:
                    guess2_row = int(input("P2 Guess row: "))
                    guess2_col = int(input("P2 Guess column:"))

                except IndexError:
                    print("Please pick a valid position:")
                    guess2_row = int(input("P2 Guess row: "))
                    guess2_col = int(input("P2 Guess column:"))

                while True:
                    if guess2_row == 0 or guess2_col == 0:
                        print("\n")
                        print("Please pick a valid position!")
                        guess2_row = int(input("P2 Guess row: "))
                        guess2_col = int(input("P2 Guess column:"))
                        continue
                    else:
                        break

                while True:
                    try:
                        if board[guess2_row - 1][guess2_col] == "✖":
                            print("\n")
                            print("You hit the ocean there before! Pick another position!")
                            guess2_row = int(input("P2 Guess row: "))
                            guess2_col = int(input("P2 Guess column:"))
                            continue
                        else:
                            break
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        guess2_row = int(input("P2 Guess row: "))
                        guess2_col = int(input("P2 Guess column:"))
                        continue

                while True:
                    try:
                        if board[guess2_row - 1][guess2_col] == "⏺":
                            print("\n")
                            print("You hit that ship once! Pick another position!")
                            guess2_row = int(input("P2 Guess row: "))
                            guess2_col = int(input("P2 Guess column:"))
                            continue
                        else:
                            break
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        guess2_row = int(input("P2 Guess row: "))
                        guess2_col = int(input("P2 Guess column:"))
                        continue

                if (s2 == [True] and guess2_row == P1ship1_row and guess2_col == P1ship1_col or
                s2 == [True] and guess2_row == P1ship2_row and guess2_col == P1ship2_col):

                    try:
                        board[guess2_row - 1][guess2_col] = "⏺"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        break
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print("All ships SANK, P2 won!")
                    game = 15

                elif (guess2_row == P1ship1_row and guess2_col == P1ship1_col or
                guess2_row == P1ship2_row and guess2_col == P1ship2_col):
                    try:
                        board[guess2_row - 1][guess2_col] = "⏺"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        continue
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    if s2:
                        print("Ship down!")
                    s2 = [True]
                    game += 1
                else:
                    try:
                        board[guess2_row - 1][guess2_col] = "✖"
                    except IndexError:
                        print("\n")
                        print("Please pick a valid position!")
                        continue
                    print("\n" * 2)
                    display_board()
                    print("\n")
                    print("Miss!")
                    game += 1
        except ValueError:
            print("You have entered an invalid character - quitting")
            rs = [False]

        if game == 15:
            modul.game_over()
            restart = input("Do you want to play one more round?(y or n) ")
            if restart == "y":
                rs = [True]
            elif restart == "n":
                rs = [False]
    elif titlescreen == "q" or titlescreen == "Q":
        break
