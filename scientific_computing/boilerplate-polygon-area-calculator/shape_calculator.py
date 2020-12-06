class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return ('Rectangle(width=%d, height=%d)' % (self.width, self.height))

  def set_width(self, val):
    self.width = val

  def set_height(self, val):
    self.height = val

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      return (('*' * self.width + '\n') * self.height)

  def get_amount_inside(self, shape):
    return ((self.width // shape.width) * (self.height // shape.height))


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def __repr__(self):
    return ('Square(side=%d)' % self.width)

  def set_width(self, val):
    self.set_side(val)

  def set_height(self, val):
    self.set_side(val)

  def set_side(self, val):
    self.width = val
    self.height = val
