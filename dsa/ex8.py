class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso")
        else:
            print("Livro indisponivel")

    def devolver(self):
        self.disponivel = True
        print("Livro devolvido com sucesso")

    def verificarDisponibilidade(self):
        if self.disponivel:
            return "Disponivel"
        return "Indisponivel"


livro = Livro("O Pequeno Principe", "Antoine de Saint-Exupery", 96)
print(livro.verificarDisponibilidade())
livro.emprestar()
print(livro.verificarDisponibilidade())
livro.devolver()
print(livro.verificarDisponibilidade())
