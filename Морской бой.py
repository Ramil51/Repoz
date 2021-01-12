from random import randint



class Dot:                                                           # Координаты точки
    def __init__(self, x, y):
        self.x = x
        self.y = y



    def __eq__(self, other):                                          # Метод сравнения координаты точки с остальными
        return self.x == other.x and self.y == other.y

#

    def __repr__(self):
        return f"({self.x}, {self.y})"


class BoardException(Exception):                                        # класс родитель всех исключений
    pass


class BoardOutException(BoardException):                       # исключения, когда пользователь стреляет за границы доски
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):                       # исключения, когда пользователь стреляет в точку, куда уже стрелял
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):                   # исключения, когда пытаемся поставить корабль на доску в недопустимое место
    pass

# класс корабль,свойства корабля : bow - нос, l - длина корабля,жизнь корабля, o - окружение корабля

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []                                    # список точкек корабля
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))             # добавляем в список точек кординаты курса

        return ship_dots

    # метод выстрела

    def shooten(self, shot):
        return shot in self.dots

        # класс борт корабля

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]       # заполнение поля корабля буквой О

        self.busy = []                                          # Ззанятые клетки
        self.ships = []                                         # количество корабпей

        # добавление кораблей

    def add_ship(self, ship):

        for d in ship.dots:                                     # точка корабля среди точек
            if self.out(d) or d in self.busy:                   # Если точка вне поля или занята
                raise BoardWrongShipException()                  # Вызываем исключение
        for d in ship.dots:                                      # если точка в пределах нормы,то ставим квадратик
            self.field[d.x][d.y] = "■"
            self.busy.append(d)                                  # заносим точку в список занятых

        self.ships.append(ship)                                  # добавление корабля
        self.contour(ship)                                       # очертим контур

    def contour(self, ship, verb=False):                          # метод определения контура корабля
        near = [
            (-1, -1), (-1, 0), (-1, 1),                           # возможные варианты точек контура
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))            # если координаты вне доски

    def shot(self, d):                                # стрельба
        if self.out(d):                               # если точка,вне доски,вызываем исключение
            raise BoardOutException()

        if d in self.busy:                            # если точка занята,тоже исключение
            raise BoardUsedException()

        self.busy.append(d)                            # добавляем точку в список занятых

        for ship in self.ships:                        # проходим циклом по списку кораблей
            if d in ship.dots:                         # если точка выстрела совпадает с точкой корабля
                ship.lives -= 1                      # жизнь корабля уменьшается на 1 на поле скоординатами ставится 'Х'
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:                   # если жизнь корабля равен 0, в счетчик добавляем 1
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."                      # если попадаем мимо корабля
        print("Мимо!")
        return False

    def begin(self):                                      # начало игры
        self.busy = []


class Player:
    def __init__(self, board, enemy):
        self.board = board                                 # доска игрока
        self.enemy = enemy                                 # доска компа

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):                                                # игрок комп
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):                                               # игрок пользователь
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:                                     # если не 2 координаты
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):                 # если ввели не числа
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]                      # список кораблей
        board = Board(size=self.size)                     # борт корабля равен размеру
        attempts = 0                                      # первоначально 0 кораблей
        for l in lens:                                    # проходим циклом по списку кораблей
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))    # экземпляр корабля
                try:
                    board.add_ship(ship)                   # еслиб корабль подходит по параметрам, добавляем корабль на доску
                    break
                except BoardWrongShipException:            # иначе вызываем исключение
                    pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):                      # цикл зарисовки досок,определение очередности хода и кто выиграл
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()                                             # запуск игры