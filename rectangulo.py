class Rectangulo:

    def __init__(self, punto_1, punto_2):
        self.punto_1 = punto_1
        self.punto_2 = punto_2

    def perimetro(self, b, h):
        P = 2 * (b + h)

    def area(self, b, h):
        A = b * h

    def cuadrado(self, b, h):
        if b == h:
            print("su cuadrado es un rectangulo")