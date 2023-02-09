import math

class Rectangle:
    def __init__(self, width, height=None):  # todo: ok
        if height is None:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def __str__(self):  # todo: ok
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)
    
    def set_width(self, width):  # todo: ok
        self.width = width

    def set_height(self, height):  # todo: ok
        self.height = height

    def get_area(self):  # todo: ok
        return self.width * self.height

    def get_perimeter(self):  # todo: ok
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):  # todo: ok
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):  # todo: ok
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for i in range(0, self.height):
                picture += '*'*self.width + '\n'
            return picture

    def get_amount_inside(self, figure):
        width, height, current_height, current_width = figure.width, figure.height, self.height, self.width
        final_width = current_width / width
        final_height = current_height / height
        if final_width >= 1 and final_height >= 1:
            return math.trunc(final_height) * math.trunc(final_width)


class Squard(Rectangle):

    def __str__(self):  # todo: ok
        return 'Square(side={})'.format(self.width)

    def set_side(self, side):  # todo: ok
        self.width = side
        self.height = side