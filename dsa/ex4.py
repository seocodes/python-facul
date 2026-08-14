class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return f"Quadrado(lado={self.lado})"

    def retornarLado(self):
        return self.lado

    def trocarLado(self, novo_lado):
        self.lado = novo_lado

    def calcularArea(self):
        return self.lado ** 2  # Potencia de 2

quadrado = Quadrado(5)
print(quadrado)
print(quadrado.retornarLado())
print(quadrado.calcularArea())
