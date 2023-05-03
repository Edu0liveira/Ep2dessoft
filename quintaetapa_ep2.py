def afundados(dicionario, tabuleiro):
    listadeafundados = 0
    for lista in dicionario.values():
        for conjunto in lista:
            pos = 0
            for posicao in conjunto:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] == 'X':
                    pos += 1
            if pos == len(conjunto):
                listadeafundados += 1
    return listadeafundados