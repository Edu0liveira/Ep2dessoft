def preenche_frota (frota, nome, linha, coluna, orientacao, tamanho):
    #frota é um dicionario
    sublista2 = []
    lista = []
    dicionario = {}

    #posicao = [x,y] vertical muda o x e horizontal muda o y,

    if frota != {}:
        for e in frota.keys():
            valor = frota[e]
            lista.append(valor)



    if orientacao == 'vertical':
        for i in range (0,tamanho):
            sublista1 = [linha+i,coluna]
            sublista2.append(sublista1)


    if orientacao == 'horizontal':
        for i in range (0,tamanho):
            sublista1 = [linha,coluna+i]
            sublista2.append(sublista1)

    lista.append(sublista2)
        
    

    dicionario[nome] = lista
    return dicionario





