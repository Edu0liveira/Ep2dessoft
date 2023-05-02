def posiciona_frota(dicionario_de_infos_dos_navios):
    
    tabuleiro = []
    for i in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)


    for valores in dicionario_de_infos_dos_navios.values():
        for posicoes in valores:

            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]

                lista_esc = tabuleiro[linha]
                lista_esc[coluna] = 1


    return tabuleiro



    



            





