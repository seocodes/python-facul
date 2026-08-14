class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def __str__(self):
        return f"Retangulo(comprimento={self.comprimento}, largura={self.largura})"

    def retornarLados(self):
        return self.comprimento, self.largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)

    def mudarLados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


retangulo = Retangulo(5, 10)
print(f"Comprimento: {retangulo.comprimento}, Largura: {retangulo.largura}")
print(f"Área: {retangulo.calcularArea()}")
print(f"Perímetro: {retangulo.calcularPerimetro()}")

retangulo.mudarLados(7, 3)
print(f"Novos lados: {retangulo.retornarLados()}")
print(f"Nova área: {retangulo.calcularArea()}")
print(f"Novo perímetro: {retangulo.calcularPerimetro()}")


