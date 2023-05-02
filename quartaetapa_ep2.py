def posiciona_frota(dicionario_de_infos_dos_navios):
    listas = 10*[0]
    tabuleiro = 10*listas

    for lista in dicionario_de_infos_dos_navios.values():
        for posicoes in lista:

            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]

                tabuleiro[linha][coluna] = 1


    return tabuleiro

#nao to entendendo o erro, ve ai 
#int object does not support item assignment



    



            





