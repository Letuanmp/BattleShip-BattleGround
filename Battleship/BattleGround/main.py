from itertools import chain
import time
from ..utils import RenderInterface as animation
import random
# from ..utils import RenderTest as animation

from ..example_submission import team1
from ..example_submission import team2

from ..Submissions import Ashit_Waghray as team1
from ..Submissions import bang_rohith_dandi as team2

dim = 10  # dimension of board
response = ""


def update_hit(board, x, y):
    global response
    info = -1
    if x >= len(board) or y >= len(board[0]) or x <= -(len(board)) or y <= -(len(board[0])):
        response = "FIRED OUT OF BATTLEZONE"
        print(response)

    elif board[x][y] == 1:
        info = 0
        board[x][y] = info
        response = "HIT !!"
        print(response)

    else:
        response = "MISS !!"
        print(response)
        info = 1  # MISS

    return (board, info)


def game_over(board):
    for i in range(10):
        for j in range(10):
            print(board[i][j], end=" ")
        print("")
    if all(x == 0 for x in chain(*board)):
        return True

    return False


def hawkeye_attack(board, x, y):
    for i in range(dim):
        if board[x][i] == 1:
            board[x][i] = 0
        if board[i][y] == 1:
            board[i][y] = 0

    return board


# Loading both Bot Programs as modules
team1_module = team1.BattleShip()
team2_module = team2.BattleShip()


# Loading team names
team1_name = team1_module.team_name
team2_name = team2_module.team_name


# Setting both BattleFields !!
team1_ships = team1_module.set_ships()
team2_ships = team2_module.set_ships()


# converting to the board to matrix format
team1_board = [[0]*10 for i in range(10)]
team2_board = [[0]*10 for i in range(10)]

for ship in team1_ships:  # Adding a redundant 0
    ship.append(1)
    ship[4] = ship[3]
    ship[3] = ship[2]
    ship[2] = 0

for ship in team2_ships:
    ship.append(1)
    ship[4] = ship[3]
    ship[3] = ship[2]
    ship[2] = 0

for ship in team1_ships:
    row = ship[0]
    col = ship[1]
    length = ship[3]
    orientation = ship[4]

    if orientation == 0:
        for i in range(length):
            team1_board[row+i][col] = 1
    elif orientation == 1:
        for i in range(length):
            team1_board[row][col+i] = 1


for ship in team2_ships:
    row = ship[0]
    col = ship[1]
    length = ship[3]
    orientation = ship[4]

    if orientation == 0:
        for i in range(length):
            team2_board[row+i][col] = 1
    elif orientation == 1:
        for i in range(length):
            team2_board[row][col+i] = 1


# For Pygame initialisation
animation.ships1 = team1_ships
animation.ships2 = team2_ships
animation.initialize()


# Randomly putting two special spots in two ships for triggering special attack !!
# Randomly putting two special spots in two ships for triggering special attack !!
special_spots = []
for i in range(dim):
    for j in range(dim):
        if team1_board[i][j] == 1:
            special_spots.append((i, j))

# Convert special_spots to a list for compatibility with random.sample
team1_special_spot = random.sample(list(special_spots), 2)

special_spots = []
for i in range(dim):
    for j in range(dim):
        if team2_board[i][j] == 1:
            special_spots.append((i, j))

team2_special_spot = random.sample(list(special_spots), 2)

#team2_special_spot = [(3,3), (3,4)]

animation.team1_special_spots = team1_special_spot
animation.team2_special_spots = team2_special_spot
print("TEAM 1 SPL SPOT : ", team1_special_spot)
print("TEAM 2 SPL SPOT : ", team2_special_spot)

team1_hawkeye_activated = False
team2_hawkeye_activated = False
# index 0 is for skipping opponent's chance and index 1 is for Missile Hawkeye!

# Player1 driver function


def player1():
    global team2_board, team2_special_spot, team1_hawkeye_activated, response
    x, y = team1_module.attack()
    print(f"{team1_name} attacked at  : " + str((x, y)))
    animation.update((y, x), isfromleft=True)  # Update Animation board

    # Updates the board as well as returns hit/miss
    team2_board, info = update_hit(team2_board, x, y)
    if team1_hawkeye_activated:
        team1_hawkeye_activated = False
        team2_board = hawkeye_attack(team2_board, x, y)
        team2.opponent_board = team2_board
    if (x, y) in team2_special_spot:
        if team2_special_spot.index((x, y)) == 0:
            info = 2
            response = f"{team1_name} NULLIFIED {team2_name}"
            print(response)

        elif team2_special_spot.index((x, y)) == 1:
            info = 3
            team1_hawkeye_activated = True
            response = "HAWKEYE ACTIVATED !! "
            print(response)

        team2_special_spot[team2_special_spot.index((x, y))] = None

    # info = 0 for only hit , 1 for miss, and -1 for out of range shooting, info = 2 for skipping opponent's chance, and info = 3 for Hawkeye Missile Activation
    team1_module.hit_or_miss(x, y, info)
    print(f"player 1: {info}")

    # #time.sleep(1)
    if game_over(team2_board):
        winner_text = f"{team1_name} has won !!!"
        animation.winner = team1_name
        animation.game_over = True
        # time.sleep(10)
        # exit()

    if info == 2:
        player1()

# Player 2 driver function
def player2():
    global team1_board, team2_board, team1_special_spot, team2_hawkeye_activated
    x, y = team2_module.attack()
    print(f"{team2_name} attacked at  : " + str((x, y)))
    animation.update((y, x), isfromleft=False)  # Update Animation board

    team1_board, info = update_hit(team1_board, x, y)
    if team2_hawkeye_activated:
        team2_hawkeye_activated = False
        team1_board = hawkeye_attack(team1_board, x, y)
        team1.opponent_board = team1_board

    if (x, y) in team1_special_spot:
        if team1_special_spot.index((x, y)) == 0:
            info = 2
            response = f"{team2_name} NULLIFIED {team1_name}"
            print(response)
            # time.sleep(5)

        elif team1_special_spot.index((x, y)) == 1:
            info = 3
            team2_hawkeye_activated = True
            response = "HAWKEYE ACTIVATED !! "
            print(response)
            # time.sleep(5)

        team1_special_spot[team1_special_spot.index((x, y))] = None

    team2_module.hit_or_miss(x, y, info)
    print(f"player 2: {info}")

    if game_over(team1_board):
        winner_text = f"{team2_name} has won !!!"
        animation.winner = team2_name
        animation.game_over = True
        print(winner_text)
        # time.sleep(10)
        # exit()

    if info == 2:
        player2()

import tkinter as tk

def start_game():
    # Close the popup window and start the game
    start_game_vs_computer()

def exit_game():
    # Close the popup window and exit the game
    root.destroy()

def start_game_vs_computer():
    global player_turn
    player_turn = 1  # 1 cho player1 (người chơi), 2 cho player2 (máy tính)

    # Đóng cửa sổ chọn chế độ chơi
    root.destroy()

    while True:
        try:
            if player_turn == 1:
                # Để player1 (người chơi) bắn
                player1()
                player_turn = 2  # Chuyển sang lượt của player2 (máy tính)
            else:
                # Để player2 (máy tính) bắn
                player2()
                player_turn = 1  # Chuyển lại lượt của player1 (người chơi)
        except Exception as e:
            print(e)
            pass


# Initialize the main Tkinter window
root = tk.Tk()
root.title("Battleship Game")
root.geometry("300x200")

# Create buttons for starting and exiting the game
button_start_game = tk.Button(root, text="Start Game", command=start_game)
button_start_game.pack(pady=20)

button_exit_game = tk.Button(root, text="Exit Game", command=exit_game)
button_exit_game.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
