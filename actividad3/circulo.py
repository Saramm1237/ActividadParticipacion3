from math import pi

class circulo:

  def __init__(self, centro, radio):
    self.centro = centro
    self.radio = radio

  def area(self):
    A = math.pi * self.radio ** 2

  def perimetro(self):
    P = 2 * math.pi * self.radio
