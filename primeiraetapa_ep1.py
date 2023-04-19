listazeros = 10*[0]

grid = 10*[listazeros]

def define_posicoes(linha,coluna,orientacao,tamanho):
    listaretorno = tamanho*[0]
    if orientacao == 'vertical':
        for i in range(len(listaretorno)):
            listaretorno[i] = [linha + i,coluna]
    if orientacao == 'horizontal':
        for i in range(len(listaretorno)):
            listaretorno[i] = [linha,coluna + i]
    return listaretorno