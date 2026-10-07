def soma_vetor(vetor):
    if not vetor:
        return 0
    return vetor[0] + soma_vetor(vetor[1:])

vetor = [5, 3, 1, 9, 2]
print(soma_vetor(vetor))
