"""Two-player command-line tic-tac-toe.

Players alternate placing their symbol (X or O) on a 3x3 grid addressed by the
numbers 0-8. A win increments the winning player's score; a full board with no
winner is settled by a rock-paper-scissors tiebreak.
"""

import random


class Input():
    """Reads and validates a player's move."""

    def __init__(self):
        pass

    def getInput(self, currentPlayer):
        """Prompt the current player for a move and return the validated value."""
        self.currentPlayer = currentPlayer
        userInput = str(input("Please enter your move player " + self.currentPlayer + ": "))
        self.isValid(userInput)
        return userInput

    def isValid(self, userInput):
        """Return the move if it is a free board position, otherwise re-prompt."""
        self.userInput = userInput
        validInputs = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        if self.userInput in validInputs:
            validInputs.remove(self.userInput)
            return self.userInput
        else:
            print("Move not valid, please try again.")
            self.getInput(self.currentPlayer)


class Player():
    """A player, identified by their symbol, with a win counter."""

    def __init__(self, symbol, wins):
        self.symbol = symbol
        self.wins = 0


class PlayerX(Player):
    """The player using symbol X."""

    def __init__(self):
        super().__init__("X", 0)


class PlayerO(Player):
    """The player using symbol O."""

    def __init__(self):
        super().__init__("O", 0)


class Board():
    """The 3x3 board: holds state, applies moves and prints itself."""

    def __init__(self, input, playerX, playerO):
        # The board is a flat list of 9 cells, indexed 0-8.
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self.input = input
        self.playerX = playerX
        self.playerO = playerO

    def editBoard(self, currentPlayer):
        """Place the current player's symbol at their chosen free position."""
        self.currentPlayer = currentPlayer
        self.input.getInput(self.currentPlayer)
        playerInput = int(self.input.userInput)
        if self.board[playerInput] == " ":
            # Cell is free: record the move and show the updated board.
            self.board[playerInput] = self.currentPlayer
            self.printBoard()
        elif self.board[playerInput] != " ":
            # Cell is taken: reject the move and re-prompt.
            print("Somebody has already moved here, try again.")
            self.editBoard(self.currentPlayer)

    def printBoard(self):
        """Print the current board as a 3x3 grid."""
        print("----" * 3 + "-")
        print("| " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " |")
        print("----" * 3 + "-")
        print("| " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " |")
        print("----" * 3 + "-")
        print("| " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " |")
        print("----" * 3 + "-\n")


class Game:
    """Coordinates the players, board and input, and runs the game loop."""

    def __init__(self, board, input, playerX, playerO):
        self.board = board
        self.input = input
        self.playerX = playerX
        self.playerO = playerO

    def rules(self):
        """Print the rules and the position numbering scheme."""
        print("Welcome to TextTacToe!")
        input("\nHere are the rules, press enter to continue.")
        input("\n1) Decide which player is X and O")
        input("\n2) Each move is decided by selecting a number between 0 - 8")
        print("\nPositions are as followed:")
        print("----" * 3 + "-")
        print("| " + "0" + " | " + "1" + " | " + "2" + " |")
        print("----" * 3 + "-")
        print("| " + "3" + " | " + "4" + " | " + "5" + " |")
        print("----" * 3 + "-")
        print("| " + "6" + " | " + "7" + " | " + "8" + " |")
        print("----" * 3 + "-")
        input("\n3) If game results in a draw, a game of Rock Paper Scissors is initiated.\n")
        input("Press enter to start...")

    def play(self):
        """Run the main game loop until a player wins or the board fills up."""
        # Choose randomly which player moves first.
        start = random.randint(1, 2)
        if start == 1:
            self.currentPlayer = playerX
            print("\nPlayer X will begin.\n")
        else:
            self.currentPlayer = playerO
            print("\nPlayer O will begin.\n")

        self.board.printBoard()
        finished = False   # set True when a round ends
        turnCounter = 0    # used to detect a full-board draw

        while finished == False:
            turnCounter += 1
            # Apply the current player's move.
            self.board.editBoard(self.currentPlayer.symbol)
            # checkGameState returns the winning symbol, or False if no win yet.
            winner = self.checkGameState(self.currentPlayer.symbol)

            if winner != False:
                finished = True
                self.currentPlayer.wins += 1
                print("Congratulations player " + winner + ", you have won!")
                print("You now have a score of: " + str(self.currentPlayer.wins) + "\n")

            # A full board with no winner is a draw, settled by rock-paper-scissors.
            if turnCounter == 9:
                if winner == False:
                    self.rps()
            # Otherwise hand the turn to the other player.
            elif self.currentPlayer == self.playerX:
                self.currentPlayer = playerO
            elif self.currentPlayer == self.playerO:
                self.currentPlayer = playerX

            if finished == True:
                self.playAgain()

    def playAgain(self):
        """Ask the players whether to start a new round."""
        userChoice = input("Would you like to play again? (y/n): ")
        if userChoice == "y":
            # Reset the board and start a fresh round.
            self.board.board = [" ", " ", " ",
                                " ", " ", " ",
                                " ", " ", " "]
            self.play()
        elif userChoice == "n":
            print("\nThanks for playing!")
        else:
            print("Please enter either y or n.")
            self.playAgain()

    def checkGameState(self, symbol):
        """Return the winning symbol if the player has three in a row, else False."""
        for i in range(3):
            # Horizontal win on row i.
            if self.board.board[(i*3)] == symbol and self.board.board[(i*3) + 1] == symbol and self.board.board[(i*3) + 2] == symbol:
                return symbol
            # Vertical win on column i.
            elif self.board.board[i] == symbol and self.board.board[i+3] == symbol and self.board.board[i+6] == symbol:
                return symbol

        # Diagonal win (top-left to bottom-right).
        if self.board.board[0] == symbol and self.board.board[4] == symbol and self.board.board[8] == symbol:
            return symbol
        # Diagonal win (top-right to bottom-left).
        elif self.board.board[2] == symbol and self.board.board[4] == symbol and self.board.board[6] == symbol:
            return symbol

        return False

    def rps(self):
        """Settle a drawn board with a rock-paper-scissors round."""
        finished = True
        validInputs = ["r", "p", "s"]

        playerXInput = str(input("Player X, please enter r (Rock), p (Paper) or s (Scissors): "))
        if playerXInput not in validInputs:
            print("Input not valid.")
            self.rps()
        # Blank lines hide player X's choice from player O.
        print("\n" * 11)

        playerOInput = str(input("Player O, please enter r (Rock), p (Paper) or s (Scissors): "))
        if playerOInput not in validInputs:
            print("Input not valid.")
            self.rps()

        # A tie restarts the tiebreak.
        if playerXInput == playerOInput:
            print("\nIt's a draw. You must play again.")
            self.rps()

        # Otherwise decide the winner and update their score.
        elif playerXInput == "r":
            if playerOInput == "s":
                print("\nPlayer X wins: rock beats scissors.")
                playerX.wins += 1
                print("Player X now has " + str(playerX.wins) + " wins.\n")
                self.playAgain()
            else:
                print("\nPlayer O wins: paper beats rock.")
                playerO.wins += 1
                print("Player O now has " + str(playerO.wins) + " wins.\n")
                self.playAgain()
        elif playerXInput == "p":
            if playerOInput == "r":
                print("\nPlayer X wins: paper beats rock.")
                playerX.wins += 1
                print("Player X now has " + str(playerX.wins) + " wins.\n")
                self.playAgain()
            else:
                print("\nPlayer O wins: scissors beats paper.")
                playerO.wins += 1
                print("Player O now has " + str(playerO.wins) + " wins.\n")
                self.playAgain()
        elif playerXInput == "s":
            if playerOInput == "p":
                print("\nPlayer X wins: scissors beats paper.")
                playerX.wins += 1
                print("Player X now has " + str(playerX.wins) + " wins.\n")
                self.playAgain()
            else:
                print("\nPlayer O wins: rock beats scissors.")
                playerO.wins += 1
                print("Player O now has " + str(playerO.wins) + " wins.\n")
                self.playAgain()


# Set up the game objects.
i = Input()
playerX = PlayerX()
playerO = PlayerO()
b = Board(i, playerX, playerO)
g = Game(b, i, playerX, playerO)

# Show the rules, then start the game.
g.rules()
g.play()
