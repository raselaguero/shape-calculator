from shape_calculator import Rectangle, Squard

rectangle = Rectangle(10, 5)
print(rectangle.get_area())
rectangle.set_height(3)
print(rectangle.get_perimeter())
print(rectangle)
print(rectangle.get_picture())

squard = Squard(9)
print(squard.get_area())
squard.set_side(4)
print(squard.get_diagonal())
print(squard)
print(squard.get_picture())

rectangle.set_height(8)
rectangle.set_width(16)
print(rectangle.get_amount_inside(squard))