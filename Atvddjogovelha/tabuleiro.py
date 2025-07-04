# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # Verifica linhas
        for linha in self.matriz:
            soma = sum(linha)
            if soma == 3:
                print("Jogador 0 ganhou!")
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                print("Jogador X ganhou!")
                return Tabuleiro.JOGADOR_X

        # Verifica colunas
        for i in range(3):
            soma = self.matriz[0][i] + self.matriz[1][i] + self.matriz[2][i]
            if soma == 3:
                print("Jogador 0 ganhou!")
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                print("Jogador X ganhou!")
                return Tabuleiro.JOGADOR_X

        # Verifica diagonais
        diagonal1 = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        diagonal2 = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if diagonal1 == 3 or diagonal2 == 3:
            print("Jogador 0 ganhou!")
            return Tabuleiro.JOGADOR_0
        elif diagonal1 == 12 or diagonal2 == 12:
            print("Jogador X ganhou!")
            return Tabuleiro.JOGADOR_X

        # Nenhum vencedor
        return Tabuleiro.DESCONHECIDO