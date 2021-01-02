board = list(range(1, 10))  # Количество клеток
# Выиграшные комбинации
wins_coord = [(1, 2, 3), (4, 5, 6,), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# Рисуем игровое поле
def draf_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


# Функция ввода значений

def take_input(playar_token):
    while True:
        value = input('Куда поставить:' + playar_token + '?')
        if not (value in '123456789'):
            print('Ошибочный вывод.Повторите.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'xo':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = playar_token
        break

    # Функция проверки

def chek_win():
        for each in wins_coord:
            if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
                return board[each[1] - 1]

        else:

            return False

# Гпавная функция


def main():
    counter = 0
    draf_board()
    while True:
        draf_board()
        if counter % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        if counter > 3:
            winner = chek_win()
            if winner:
                draf_board()
                print(winner, "выиграл!")
                break
        counter += 1
        if counter > 8:
            draf_board()
            print('Ничья!')
            break


main()

