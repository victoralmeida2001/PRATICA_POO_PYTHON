class FormaGeonetrica:
    def __init__(self, calcular_area, calcular_perimetro):
        self.calcular_area = calcular_area
        self.calcular_perimetro = calcular_perimetro
        

class Retangulo(FormaGeonetrica):
    def __init__ (self, altura, largura):
        super().__init__(altura, largura)
        self.altura = altura
        self.largura = largura
    def calculo_geometrico(self):
        print('-'*10)
        print(f'A área do Retangulo é = {self.altura * self.largura} cm²')
        print(f'O perimetro do Retangulo é = {(self.altura ** 2) + (self.largura ** 2)} cm')
        print('-'*10)

class Circulo(FormaGeonetrica):
    def __init__(self, raio):
        super().__init__(raio, 3.14)
        self.raio = raio
    
    def calculo_geometrico(self):
        print('-'*10)
        print(f'A área do Circulo é = {3.14 * (self.raio ** 2)} cm²')
        print(f'O perimetro do Circulo é = {2 * 3.14 * self.raio} cm')
        print('-'*10)



dado = Retangulo (6, 8)
dado.calculo_geometrico()

adesivo = Circulo (15)
adesivo.calculo_geometrico()

d1 = Retangulo (5, 5)
d1.calculo_geometrico()

a1 = Circulo (3)
a1.calculo_geometrico()

d2 = Retangulo (6, 40)
d2.calculo_geometrico()

a2 = Circulo (80)
a2.calculo_geometrico()