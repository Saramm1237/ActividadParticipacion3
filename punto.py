from math import sqrt

class Punto:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def mostrar(self):
    print(f"las coordenadas en x son {self.x} y en y {self.y}")

  def mover(slef, new_x, new_y):
    self.x += new_x
    self.y += new_y

  def calcular_distancia(self, x_2, y_2):
    D = math.sqrt((x_2 - self.x) ** 2 + (y_2 - self.y) ** 2)