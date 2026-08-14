from re import A


class Aluno:
    def __init__(self, nome, nota1, nota2, media=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media

    # Opcionalmente, usei __str__ como metodo para mostrar todos os dados -> nao seria igual criar um
    # metodo específico para mostrar os dados, mas é uma forma conveniente de mostrar
    # a representação em string do objeto
    def __str__(self):
        return f"Aluno: {self.nome}, Nota 1: {self.nota1}, Nota 2: {self.nota2}, Média: {self.media}"

    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def verificarAprovacao(self):
        if self.media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

    def mostrarDados(self):
        print(f"Nome: {self.nome}, \nNota 1: {self.nota1}, \nNota 2: {self.nota2}, \nMédia: {self.media}")

aluno1 = Aluno("Augusto", 7, 8)
aluno2 = Aluno("Arthur", 5, 6)

aluno1.calcularMedia()
aluno2.calcularMedia()

print(aluno1.verificarAprovacao())
print(aluno2.verificarAprovacao())

aluno1.mostrarDados()
aluno2.mostrarDados()

# Opcao com o def __str__ seria assim:
# print(aluno1)
# print(aluno2)
