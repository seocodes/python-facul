class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


pessoa = Pessoa("Augusto", 19, 70, 175)
pessoa.envelhecer()
pessoa.engordar(2)
pessoa.emagrecer(1)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade} anos")
print(f"Peso: {pessoa.peso} kg")
print(f"Altura: {pessoa.altura} cm")
