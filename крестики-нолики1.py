class Board_game():
    def __init__(self):
        self.wins_coord = [(1, 2, 3), (4, 5, 6,), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        self.board = list(range(1, 10))


    def draf_board(self):

        print('-------------')
        for i in range(3):
            print('|', self.board[0 + i * 3], '|', self.board[1 + i * 3], '|', self.board[2 + i * 3], '|')
        print('-------------')



    def take_input(self,playar_token):
        while True:
            value = input('Куда поставить: '+playar_token + '?')
            if not (value in '123456789'):
                print('Ошибочный вывод.Повторите.')
                continue
            value = int(value)
            if str(self.board[value - 1]) in 'xo':
                print('Эта клетка уже занята')
                continue
            self.board[value - 1] = playar_token
            break

    def chek_win(self):

        for each in self.wins_coord:
            if (self.board[each[0] - 1]) == (self.board[each[1] - 1]) == (self.board[each[2] - 1]):
                return self.board[each[1] - 1]
        else:
            return False


    def main(self):

        counter = 0
        while True:
            self.draf_board()
            if counter % 2 == 0:
                self.take_input('x')
            else:
                self.take_input('o')
            if counter > 3:
                winner = self.chek_win()
                if winner:
                    self.draf_board()
                print(winner, "выиграл!")
                break
            counter += 1
            if counter > 8:
                self.draf_board()
                print('Ничья!')
                break

g = Board_game()
g.main()