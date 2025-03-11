def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto: #enquanto nao achou o elemento central
        meio = int((baixo + alto) / 2) # verifica o elemento central
        chute = lista[meio]
        if chute == item: #acha o item
            return meio
        if chute > item: #chute muito alto
            alto = meio - 1
        else: #chute muito baixo
            baixo = meio + 1
    return None # item nao existe

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))
