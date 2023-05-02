def posiciona_frota(dicionario_de_infos_dos_navios):
    listas = 10*[0]
    tabuleiro = 10*listas

    for lista_posicoes in dicionario_de_infos_dos_navios.values():

        for posicao in lista_posicoes:
            linha = posicao[0]
            coluna = posicao[1]

            tabuleiro[linha][coluna] = 1


    return tabuleiro

#nao to entendendo o erro, ve ai 



    



            





