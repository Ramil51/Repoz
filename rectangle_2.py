from rectangle import Rectangle, Square, Circle

# далее создаем два прямоугольника и  два круга

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
circ_1 = Circle(3.14, 4)
circ_2 = Circle(3.14, 7)

# вывод площадей наших фигур

print(rect_1.get_area())
print(rect_2.get_area())
print(circ_1.get_area_circle())
print(circ_2.get_area_circle())

square_1 = Square(5)
square_2 = Square(10)
circle_3 = Circle(3.14, 4)
circle_4 = Circle(3.14, 6)

print(square_1.get_area_square(),
      square_2.get_area_square(), circle_3.get_area_circle(), circle_4.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_3, circle_4]
for figure in figures:
    if isinstance(figure, Circle):
        print(figure.get_area_circle())
    if isinstance(figure, Square):
        print(figure.get_area_square())
  

