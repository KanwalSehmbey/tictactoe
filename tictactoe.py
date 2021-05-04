
class Board:
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def check_valid_move(self, x, y):

        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        elif self.board[x][y] != " ":
            return False

        return True

    def make_move(self, player, location):
        x = int(location[0])
        y = int(location[1])
        if self.check_valid_move(x, y):
            self.board[x][y] = player
            self.print_board()
            return True
        else:
            return False

    def game_win(self):

        # all rows
        for x in range(len(self.board)):
            if self.board[x][0] == self.board[x][1] == self.board[x][2] != " ":
                return True
        #if self.board[1][0] == self.board[1][1] == self.board[1][2] != " ":
        #    return True
        #if self.board[2][0] == self.board[2][1] == self.board[2][2] != " ":
        #    return True
        # all cols
        for y in range(len(self.board)):
            if self.board[0][y] == self.board[1][y] == self.board[2][y] != " ":
                return True
        #if self.board[0][1] == self.board[1][1] == self.board[2][1] != " ":
        #    return True
        #if self.board[0][2] == self.board[1][2] == self.board[2][2] != " ":
        #    return True
        # diagonal check
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False


class Game:
    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1
        self.myBoard = Board()
        self.number_of_moves = 0
        # self.receive_move()

    def game_over(self):
        if self.number_of_moves >= 3:
            if self.myBoard.game_win():
                print(f"Game WON by player: {self.current_player}")
                return True

        if self.number_of_moves >= 9:
            return True

        return False

    def receive_move(self):

        move = input('Please input your move: ')
        result = self.myBoard.make_move(self.current_player, move)

        if result:
            self.number_of_moves += 1
        else:
            print("Invalid move, please enter a valid move")

        if self.game_over():
            print("Game over")
            exit(0)
        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
            self.receive_move()

        return


def main():

    mygame = Game()
    mygame.receive_move()


if __name__ == '__main__':
    main()

