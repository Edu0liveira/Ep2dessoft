def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    # x é linha e y é coluna
    #frota é um dicionario

    dc_final = {}
    lista_final = [] # vai pro dc final
    sublista = [] # vai pra lista_final

    for j in frota.keys():
        if j == nome_navio:
            valor = frota[j]
            lista_final.append

    for i in range(0,tamanho):
        if orientacao == 'vertical':
            lista_i = [linha+i, coluna]
            sublista.append(lista_i)

        if orientacao == 'horizontal':
            lista_i = [linha, coluna+i]
            sublista.append(lista_i)



    lista_final.append(sublista)
    dc_final[nome_navio] = lista_final

    return dc_final