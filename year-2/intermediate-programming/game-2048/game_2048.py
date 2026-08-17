"""Command-line 2048.

Move the tiles on a 4x4 grid with w/a/s/d. Matching numbers that collide merge
into their sum; a new 2 or 4 appears after each move. The goal is to reach 2048.
"""

import random


class Board:
    """The 4x4 grid: holds state, applies moves and prints itself."""

    def __init__(self):
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0],
                      [0, 0, 0, 0], [0, 0, 0, 0]]

    def makeBoard(self):
        """Place a 2 or 4 on a random free cell, then print the board."""
        addedValues = [2, 4]
        val = addedValues[random.randint(0, 1)]
        randRow = random.randint(0, 3)
        randVal = random.randint(0, 3)
        if self.board[randRow][randVal] == 0:
            self.board[randRow][randVal] = val
        elif self.board[randRow][randVal] != 0:
            self.board[randRow][randVal] = self.board[randRow][randVal]
            # Cell was occupied: retry on another random cell.
            self.makeBoard()

        # Build each row as a printable string.
        r1 = ["| " + str(self.board[0][0]) + " | " + str(self.board[0][1])
              + " | " + str(self.board[0][2]) + " | " + str(self.board[0][3]) + " |"]
        r2 = ["| " + str(self.board[1][0]) + " | " + str(self.board[1][1])
              + " | " + str(self.board[1][2]) + " | " + str(self.board[1][3]) + " |"]
        r3 = ["| " + str(self.board[2][0]) + " | " + str(self.board[2][1])
              + " | " + str(self.board[2][2]) + " | " + str(self.board[2][3]) + " |"]
        r4 = ["| " + str(self.board[3][0]) + " | " + str(self.board[3][1])
              + " | " + str(self.board[3][2]) + " | " + str(self.board[3][3]) + " |"]
        print("----" * 4 + "-")
        for i in r1:
            print(i)
        print("----" * 4 + "-")
        for j in r2:
            print(j)
        print("----" * 4 + "-")
        for k in r3:
            print(k)
        print("----" * 4 + "-")
        for l in r4:
            print(l)
        print("----" * 4 + "-")

    # The four move methods slide tiles in one direction, merging equal
    # neighbours and pulling tiles into any freed cells.

    def up(self):
        """Slide all tiles up, merging equal neighbours."""
        for i in range(4):
            for j in range(2, -1, -1):
                self.board[j][i] = self.board[j][i]
                self.board[j+1][i] = self.board[j+1][i]
                if self.board[j+1][i] == self.board[j][i]:
                    self.board[j][i] = self.board[j+1][i] * 2
                    self.board[j+1][i] = 0
                elif self.board[j][i] == 0:
                    self.board[j][i] = self.board[j+1][i]
                    self.board[j+1][i] = 0

    def left(self):
        """Slide all tiles left, merging equal neighbours."""
        for i in range(4):
            for j in range(2, -1, -1):
                self.board[i][j] = self.board[i][j]
                self.board[i][j+1] = self.board[i][j+1]
                if self.board[i][j+1] == self.board[i][j]:
                    self.board[i][j] = self.board[i][j] * 2
                    self.board[i][j+1] = 0
                elif self.board[i][j] == 0:
                    self.board[i][j] = self.board[i][j+1]
                    self.board[i][j+1] = 0

    def down(self):
        """Slide all tiles down, merging equal neighbours."""
        for i in range(4):
            for j in range(3):
                self.board[j][i] = self.board[j][i]
                self.board[j+1][i] = self.board[j+1][i]
                if self.board[j][i] == self.board[j+1][i]:
                    self.board[j+1][i] = self.board[j][i] * 2
                    self.board[j][i] = 0
                elif self.board[j+1][i] == 0:
                    self.board[j+1][i] = self.board[j][i]
                    self.board[j][i] = 0

    def right(self):
        """Slide all tiles right, merging equal neighbours."""
        for i in range(4):
            for j in range(3):
                self.board[i][j] = self.board[i][j]
                self.board[i][j+1] = self.board[i][j+1]
                if self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j+1] = self.board[i][j] * 2
                    self.board[i][j] = 0
                elif self.board[i][j+1] == 0:
                    self.board[i][j+1] = self.board[i][j]
                    self.board[i][j] = 0


class Game:
    """Coordinates the board and input, and starts the game."""

    def __init__(self, board, uInput):
        self.board = board
        self.uInput = uInput

    def greet(self):
        """Print the rules and wait for the player to start."""
        print("Welcome to 2048!")
        print("Use w, a, s or d to move all numbers on the board.")
        print("Lowercase only, press enter to confirm a move.")
        print("Combine matching numbers to add them together.")
        print("The goal is to reach 2048; you lose when no valid moves remain.")
        input("Press enter to play...")

    def play(self):
        """Show the rules, place the first tile and begin reading moves."""
        self.greet()
        self.board.makeBoard()
        self.uInput.getInput()


class uInput:
    """Reads and validates the player's move, then applies it to the board."""

    def __init__(self, board):
        self.board = board

    def getInput(self):
        """Prompt for a move and pass it to the validator."""
        userInput = input("Please enter your move: ")
        self.isValid(userInput)
        return userInput

    def isValid(self, userInput):
        """Apply a valid w/a/s/d move to the board, otherwise re-prompt."""
        self.userInput = userInput
        validInputs = ["w", "a", "s", "d"]
        if self.userInput not in validInputs:
            print("Move not valid, please try again.")
            self.getInput()
        elif self.userInput == "w":
            self.board.up()
            self.board.makeBoard()
            self.getInput()
        elif self.userInput == "a":
            self.board.left()
            self.board.makeBoard()
            self.getInput()
        elif self.userInput == "s":
            self.board.down()
            self.board.makeBoard()
            self.getInput()
        elif self.userInput == "d":
            self.board.right()
            self.board.makeBoard()
            self.getInput()


# Set up the game objects and start.
pBoard = Board()
puInput = uInput(pBoard)
g = Game(pBoard, puInput)
g.play()
