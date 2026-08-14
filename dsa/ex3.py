class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return f"Bola(cor={self.cor}, circunferencia={self.circunferencia}, material={self.material})"

    def trocarCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        print(self.cor)

bola = Bola("vermelho", 15, "couro")
print(bola)

bola.trocarCor("azul")
print(bola)  # Cor diferente
