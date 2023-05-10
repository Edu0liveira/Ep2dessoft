# função para imprimir os tabuleiros
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

# uma lista que vai ser usada laaa na frente
posicoes_escolhidas = []

# outra função..
def faz_jogada(tabuleiro, linha, coluna):
    lista_esc = tabuleiro[linha]
    casa_esc = lista_esc[coluna]
    if casa_esc == 1:
        lista_esc[coluna] = 'X'
    else:
        lista_esc[coluna] = '-'
    return tabuleiro

# mais uma
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

# função para posicionar a frota
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

# frota do oponente
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

# posiciona a frota do oponente
tabuleiro_oponente = posiciona_frota(frota_oponente)

# inicializa tabuleiro do jogador

"""
tabuleiro_jogador = []
for i in range(10):
    linha = ['0'] * 10
    tabuleiro_jogador.append(linha)
"""

dados_jogador = input('')
dicionario_jogador = {dados_jogador}
tabuleiro_jogador = posiciona_frota(dicionario_jogador)

# lista auxiliar para armazenar posições já informadas pelo jogador
posicoes_informadas = []

# loop principal do jogo
jogando = True
while jogando:
    # imprime os tabuleiros
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # pergunta a linha que o jogador deseja atacar
    linha = input('Informe a linha que deseja atacar (0 a 9): ')
    while linha not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Linha inválida!')
        linha = input('Informe a linha que deseja atacar (0 a 9): ')

    # pergunta a coluna que o jogador deseja atacar
    coluna = input('Informe a coluna que deseja atacar (0 a 9): ')
    while coluna not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Coluna inválida!')
        coluna = input('Informe a coluna que deseja atacar (0 a 9): ')

    # valida se a posição informada já foi escolhida anteriormente
    if [linha, coluna] in posicoes_escolhidas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    else:
        posicoes_escolhidas.append([linha, coluna])

    # adiciona a posição escolhida à lista de posições escolhidas
    posicoes_escolhidas.append([linha, coluna])

    # atualiza o tabuleiro do oponente com a jogada do jogador
    faz_jogada(tabuleiro_oponente, int(linha), int(coluna))

    # verifica se o jogador afundou todos os navios do oponente
    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False