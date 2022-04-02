import random

class BattleShip:
    def __init__(self):
        self.team_name = "Team 2"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1

    def set_ships(self):
        return self.ships

    def attack(self):
        x = random.randint(0,9)
        y = random.randint(0,9)

        return (x,y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info


ships = [
 [3, 3, 3, 1],
 [4, 3, 4, 0],
 [5, 8, 4, 0],
 [1, 1, 5, 1],
 [9, 1, 5, 1]]
        



opponent_board = [
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
        [-1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1],
    ]