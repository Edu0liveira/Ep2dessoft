def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    # x é linha e y é coluna
    #frota é um dicionario

    lista_final = [] # vai pro dc final
    lista = [] # vai pra lista_final

    for i in range(0,tamanho):
        if orientacao == 'vertical':
            lista_i = [linha+i, coluna]
            lista.append(lista_i)

        if orientacao == 'horizontal':
            lista_i = [linha, coluna+i]
            lista.append(lista_i)


    if nome_navio in frota:
        frota[nome_navio].append(lista)
    else:
        lista_final.append(lista)
        frota[nome_navio] = lista_final

    return frota