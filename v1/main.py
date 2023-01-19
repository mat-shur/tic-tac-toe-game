import random


class Move:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return 1 <= self._value <= 9

    def get_row(self):
        if self.value in (1, 2, 3):
            return 0
        elif self.value in (4, 5, 6):
            return 1
        else:
            return 2

    def get_column(self):
        if self.value in (1, 4, 7):
            return 0
        elif self.value in (2, 5, 8):
            return 1
        else:
            return 2


class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    @staticmethod
    def get_human_move():
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)

            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")

        return move

    @staticmethod
    def get_computer_move():
        random_choice = random.choice(range(1, 10))
        move = Move(random_choice)

        print("Computer move (1-9): ", move.value)

        return move


class Board:
    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def print_board(self):
        print("\nPositions:")

        self.print_board_with_positions()

        print("Board:")

        for row in self.game_board:
            print("|", end="")

            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")

            print()

        print()

    @staticmethod
    def print_board_with_positions():
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already taken. Please enter another one.")

    def check_is_game_over(self, player, last_move):
        return (self.check_row(player, last_move)
                or (self.check_column(player, last_move))
                or (self.check_diagonal(player))
                or (self.check_antidiagonal(player)))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3

    def check_column(self, player, last_move):
        markers_count = 0
        column_index = last_move.get_column()

        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_antidiagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][2 - i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_is_tie(self):
        empty_counter = 0

        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)

        return empty_counter == 0

    def reset_board(self):
        self.game_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]


class TicTacToe:
    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie! 👍 Try again.")
                    break
                elif board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game! 🎉")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops... 😱 The Computer Won. Try again.")
                        break

            play_again = input("Would you like to play again? Enter X for YES or O for NO: ").upper()

            if play_again == "O":
                print("Bye! Come back soon 👋")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again. 💡")
                self.start_new_round(board)

    @staticmethod
    def start_new_round(board):
        print("*************")
        print("  New Round  ")
        print("*************")
        board.reset_board()
        board.print_board()


game = TicTacToe()
game.start()
