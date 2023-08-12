from random import randint
from Personagens import Personagem


class Heroi(Personagem):
    def __init__(self, nome, raca, classe):
        super().__init__(nome, raca, classe)

        self.stat_vitorias = 0
        self.stat_derrotas = 0
        self.stat_partidas_jogadas = 0
        self.gold = 0

    def get_vitorias(self):
        return self.vitorias

    def add_vitoria(self):
        self.vitorias += 1

    def get_derrotas(self):
        return self.derrotas

    def add_derrota(self):
        self.derrotas += 1

    def get_partidas(self):
        return self.partidas_jogadas

    def add_partida(self):
        self.partidas_jogadas += 1

    def revive(self):
        self.vivo = True

    def add_xp(self, qtd):
        self.xp += qtd

    def add_xp_max(self, qtd):
        self.XP_MAX + qtd

    def set_xp_max(self, valor):
        self.XP_MAX = valor

    def set_hp_max(self, valor):
        self.HP_MAX = valor
