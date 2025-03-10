# Crie uma lista apenas com elementos numéricos
numericos = [1, 2, 3, 6, 5, 4]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
misto = ['string', 132, ['lista', 'de', 'listas']]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(numericos[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(misto[::2])

# Remova da lista o último item
print(numericos.pop())

# Insira na lista um novo item
misto.append('Abacate')
print(misto)

# Remova da lista um item específico
numericos.remove(3)
print(numericos)