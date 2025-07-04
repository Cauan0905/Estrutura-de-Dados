# -*- coding: utf-8 -*-
from random import choice

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

    def getJogada(self) -> (int, int):
        # Regra R1: Bloqueio ou vitória imediata
        jogada = self.verifica_dupla(self.tipo)
        if jogada:
            return jogada
        jogada = self.verifica_dupla(self.oponente)
        if jogada:
            return jogada

        # Regra R2: Criar duas duplas ao mesmo tempo
        jogada = self.criar_duplas()
        if jogada:
            return jogada

        # R3: Centro
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Canto oposto
        cantos_opostos = [((0, 0), (2, 2)), ((0, 2), (2, 0)), ((2, 0), (0, 2)), ((2, 2), (0, 0))]
        for (a, b) in cantos_opostos:
            if self.matriz[a[0]][a[1]] == self.oponente and self.matriz[b[0]][b[1]] == Tabuleiro.DESCONHECIDO:
                return b

        # R5: Qualquer canto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        cantos_livres = [pos for pos in cantos if self.matriz[pos[0]][pos[1]] == Tabuleiro.DESCONHECIDO]
        if cantos_livres:
            return choice(cantos_livres)

        # R6: Qualquer espaço livre
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)
        return None  # Deu velha

    def verifica_dupla(self, jogador):
        # Verifica todas as linhas, colunas e diagonais
        for i in range(3):
            # Linhas
            linha = self.matriz[i]
            if linha.count(jogador) == 2 and linha.count(Tabuleiro.DESCONHECIDO) == 1:
                return (i, linha.index(Tabuleiro.DESCONHECIDO))

            # Colunas
            coluna = [self.matriz[0][i], self.matriz[1][i], self.matriz[2][i]]
            if coluna.count(jogador) == 2 and coluna.count(Tabuleiro.DESCONHECIDO) == 1:
                return (coluna.index(Tabuleiro.DESCONHECIDO), i)

        # Diagonal principal
        diag1 = [self.matriz[i][i] for i in range(3)]
        if diag1.count(jogador) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
            idx = diag1.index(Tabuleiro.DESCONHECIDO)
            return (idx, idx)

        # Diagonal secundária
        diag2 = [self.matriz[i][2 - i] for i in range(3)]
        if diag2.count(jogador) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
            idx = diag2.index(Tabuleiro.DESCONHECIDO)
            return (idx, 2 - idx)

        return None

    def criar_duplas(self):
        # Estrategicamente verifica se há jogadas que criam múltiplas possibilidades futuras (simplificada)
        possibilidades = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    dupla = self.verifica_dupla(self.tipo)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if dupla:
                        possibilidades.append((l, c))
        if possibilidades:
            return choice(possibilidades)
        return None