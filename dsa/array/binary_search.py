import numpy as np


class VetorOrdenado:
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
      return

    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    self.valores[posicao] = valor
    self.ultima_posicao += 1

  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
    return -1

  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    while limite_inferior <= limite_superior:
      posicao_atual = (limite_inferior + limite_superior) // 2

      if self.valores[posicao_atual] == valor:
        return posicao_atual
      if self.valores[posicao_atual] < valor:
        limite_inferior = posicao_atual + 1
      else:
        limite_superior = posicao_atual - 1

    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)

    if posicao == -1:
      return -1

    for i in range(posicao, self.ultima_posicao):
      self.valores[i] = self.valores[i + 1]

    self.ultima_posicao -= 1


def main():
  vetor = VetorOrdenado(7)

  vetor.insere('a')
  vetor.insere('u')
  vetor.insere('g')
  vetor.insere('u')
  vetor.insere('s')
  vetor.insere('t')
  vetor.insere('o')

  print('Vetor ordenado:')
  vetor.imprime()

  print('\nPesquisa linear:')
  print('a:', vetor.pesquisar('a'))
  print('g:', vetor.pesquisar('g'))
  print('t:', vetor.pesquisar('t'))

  print('\nPesquisa binária:')
  print('a:', vetor.pesquisa_binaria('a'))
  print('g:', vetor.pesquisa_binaria('g'))
  print('t:', vetor.pesquisa_binaria('t'))

  vetor.excluir('a')
  vetor.excluir('s')
  vetor.excluir('u')

  print('\nVetor após as exclusões:')
  vetor.imprime()


if __name__ == '__main__':
  main()
