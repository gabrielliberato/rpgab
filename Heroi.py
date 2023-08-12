from random import randint
from Personagens import Personagem


class Heroi(Personagem):
    def __init__(self, nome, raca, classe):
        super().__init__(nome, raca, classe)

        self.stat_vitorias = 0
        self.stat_derrotas = 0
        self.stat_partidas_jogadas = 0
        self.gold = 0
        self._tipo = 'eu'

    def get_vitorias(self):
        return self.stat_vitorias

    def add_vitoria(self):
        self.stat_vitorias += 1

    def get_derrotas(self):
        return self.stat_derrotas

    def add_derrota(self):
        self.stat_derrotas += 1

    def get_partidas(self):
        return self.stat_partidas_jogadas

    def add_partida(self):
        self.stat_partidas_jogadas += 1

    def revive(self):
        self.vivo = True

    def add_xp(self, qtd):
        self._xp += qtd

    def add_xp_max(self, qtd):
        self._XP_MAX + qtd

    def set_xp_max(self, valor):
        self._XP_MAX = valor

    def set_hp_max(self, valor):
        self._HP_MAX = valor
