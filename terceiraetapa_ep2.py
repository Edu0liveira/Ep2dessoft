def faz_jogada(tabuleiro, linha, coluna):
    lista_esc = tabuleiro[linha]
    casa_esc = lista_esc[coluna]
    if casa_esc == 1:
        lista_esc[coluna] = 'X'
    else:
        lista_esc[coluna] = '-'
    return tabuleiro
