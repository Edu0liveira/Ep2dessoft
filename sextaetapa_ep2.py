def define_posicoes(linha,coluna,orientacao,tamanho):
    listaretorno = tamanho*[0]
    if orientacao == 'vertical':
        for i in range(len(listaretorno)):
            listaretorno[i] = [linha + i,coluna]
    if orientacao == 'horizontal':
        for i in range(len(listaretorno)):
            listaretorno[i] = [linha,coluna + i]
    return listaretorno



def posicao_valida (frota,linha,coluna,orientacao,tamanho):

    listapos = define_posicoes(linha,coluna,orientacao,tamanho)

    for lista in frota.values():
        for conjunto in lista:
            for coord in conjunto:
                if coord in listapos:
                    return False 

    for coord1 in listapos:
        if coord1[0] > 9 or coord1[1] > 9 or coord1[0] < 0 or coord1[1] < 0:
            return False
      


    return True
