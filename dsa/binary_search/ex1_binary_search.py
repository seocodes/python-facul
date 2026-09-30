import numpy as np


class VetorOrdenado:
  def __init__(self, capacidade):
    """Cria um vetor com tamanho fixo e inicialmente sem valores válidos."""

    self.capacidade = capacidade

    # last index ocupado. -1 é o sinal (sentinel) de que o vetor está vazio.
    self.ultima_posicao = -1

    # Reserva todo o espaço, mas apenas os indexes de 0 até ultima_posicao
    # fazem parte do vetor lógico.
    self.valores = np.empty(self.capacidade, dtype=str)

  def imprime(self):
    """Mostra somente a parte ocupada do vetor."""

    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      # range não inclui o limite final; por isso usamos last index + 1.
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    """Insere ``valor`` na posição certa, mantendo o vetor ordenado.

    Modelo mental: encontre o lugar do novo valor, abra uma vaga empurrando
    os maiores para a direita e, então, encaixe o valor nessa vaga.
    """

    # Se o last index já é capacidade - 1, não existe espaço livre.
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return

    # insertion index: primeira posição com um valor maior que o novo.
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break

      # Se chegamos ao fim sem achar um maior, o novo valor entra depois dele.
      if i == self.ultima_posicao:
        posicao = i + 1

    # Abre a vaga da direita para a esquerda. Essa ordem evita sobrescrever
    # um valor antes de ele ser movido.
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    # Encaixa o novo valor e expande em uma posição a parte ocupada.
    self.valores[posicao] = valor
    self.ultima_posicao += 1

  def pesquisar(self, valor):
    """Faz uma linear search e retorna o index de ``valor`` ou -1.

    Aqui visitamos os valores da esquerda para a direita: O(n) no pior caso.
    """

    for i in range(self.ultima_posicao + 1):
      # Como o vetor está ordenado, passar do alvo significa que ele não existe.
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i

    # Percorremos toda a parte ocupada sem encontrar o alvo.
    return -1

  def pesquisa_binaria(self, valor):
    """Retorna o index de ``valor`` (valor dado pelo usuário) ou -1 quando ele não existe.

    Modelo mental: imagine uma janela sobre o vetor ordenado. A cada rodada,
    olhamos o meio (mid) e fechamos metade da janela onde o alvo não pode estar.
    Por cortar o problema pela metade, a busca custa O(log n).
    """

    # A busca binária só funciona porque os valores estão em ordem.
    # low/left e high/right delimitam a janela que ainda pode conter o alvo.
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    # Enquanto a janela tiver ao menos uma posição, ainda há onde procurar.
    while limite_inferior <= limite_superior:
      # mid: index do elemento no meio da janela (// mantém o resultado inteiro).
      posicao_atual = (limite_inferior + limite_superior) // 2

      # Acertou o meio: missão cumprida.
      if self.valores[posicao_atual] == valor:
        return posicao_atual

      # O meio é menor que o alvo: descarte o meio e toda a metade esquerda.
      if self.valores[posicao_atual] < valor:
        limite_inferior = posicao_atual + 1
      else:
        # O meio é maior que o alvo: descarte o meio e toda a metade direita.
        limite_superior = posicao_atual - 1

    # low passou de high: a janela fechou sem encontrar o alvo.
    return -1

  def excluir(self, valor):
    """Exclui a primeira ocorrência de ``valor`` ou retorna -1 se não existir.

    Modelo mental: ao retirar alguém de uma fila, todos à direita dão um
    passo para a esquerda para fechar o espaço vazio.
    """

    # Primeiro, precisamos descobrir qual index será removido.
    posicao = self.pesquisar(valor)

    if posicao == -1:
      return -1

    # Fecha o espaço copiando cada próximo valor uma casa para a esquerda.
    for i in range(posicao, self.ultima_posicao):
      self.valores[i] = self.valores[i + 1]

    # O vetor lógico encolhe; qualquer dado além do novo last index é ignorado.
    self.ultima_posicao -= 1


def main():
  """Monta um pequeno cenário para demonstrar todas as operações."""

  vetor = VetorOrdenado(7)

  # Mesmo inseridos fora de ordem, os valores são guardados em ordem crescente.
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
  # O retorno é o index. Se houver valores repetidos, qualquer ocorrência
  # encontrada é válida; seriam necessários ajustes para exigir a 1ª ou a última.
  print('a:', vetor.pesquisa_binaria('a'))
  print('g:', vetor.pesquisa_binaria('g'))
  print('t:', vetor.pesquisa_binaria('t'))

  # Exclusões de caracteres do início, meio e final do vetor.
  vetor.excluir('a')
  vetor.excluir('s')
  vetor.excluir('u')

  print('\nVetor após as exclusões:')
  vetor.imprime()


if __name__ == '__main__':
  main()
