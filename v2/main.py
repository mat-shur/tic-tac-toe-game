import random


class TicTacToe:
    def __init__(self, player_1, player_2):
        self._board = [[' ' for _ in range(3)] for _ in range(3)]
        self._players = {}
        self._random_players_marks(player_1, player_2)

    def _random_players_marks(self, player_1, player_2):
        marks, players = ['X', 'O'], [player_1, player_2]
        self._players[players.pop(random.randint(0, 1))] = marks.pop(random.randint(0, 1))
        self._players[players[0]] = marks[0]

    def _move(self, player_name, mark):
        while True:
            try:
                row = int(input(f"{player_name} '{mark}', enter row (0, 1, 2): "))
                col = int(input(f"{player_name} '{mark}', enter col (0, 1, 2): "))

                if row in range(3) and col in range(3):
                    if self._board[row][col] == ' ':
                        break
                    else:
                        print("This space occupied, try again.")
                else:
                    print("Invalid input, try again.")
            except ValueError:
                print("Invalid input, try again.")

        self._board[row][col] = mark

    def _display_board(self):
        print()
        for row in self._board:
            print(" | ".join(row))
        print()

    def _check_game(self):
        # Rows:
        for i in range(3):
            if self._board[i][0] == self._board[i][1] == self._board[i][2] and self._board[i][0] != ' ':
                return self._board[i][0]

        # Columns:
        for i in range(3):
            if self._board[0][i] == self._board[1][i] == self._board[2][i] and self._board[0][i] != ' ':
                return self._board[0][i]

        # Diagonals:
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[0][0] != ' ':
            return self._board[0][0]

        if self._board[0][2] == self._board[1][1] == self._board[2][0] and self._board[0][2] != ' ':
            return self._board[0][2]

        # Tie (full board):
        flag = True

        for row in self._board:
            for val in row:
                if val == ' ':
                    flag = False

        if flag:
            return 'Tie'

        return None

    def start(self):
        print("Game is started!")

        status = None

        while not status:
            self._display_board()
            self._move(next(iter(self._players)), self._players[next(iter(self._players))])
            self._players = dict(reversed(list(self._players.items())))
            status = self._check_game()

        self._display_board()

        if status == 'Tie':
            print("Nobody won.")
        else:
            print(f"{next(reversed(self._players))} wins!")

        print("\nGame ended!")


game = TicTacToe('Matthew', 'Andrew')
game.start()
