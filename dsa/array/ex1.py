import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=str)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])
  
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor

  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)

    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]

      self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(7)

vetor.insere('a')
vetor.insere('u')
vetor.insere('g')
vetor.insere('u')
vetor.insere('s')
vetor.insere('t')
vetor.insere('o')

vetor.imprime()

print('\nPesquisa:') # \n para pular linha e separar da impressão do vetor
print('a:', vetor.pesquisar('a'))
print('g:', vetor.pesquisar('g'))
print('t:', vetor.pesquisar('t'))

vetor.excluir('a')
vetor.excluir('s')
vetor.excluir('o')

# Print após exclusões
vetor.imprime()