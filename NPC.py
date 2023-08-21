from Personagens import Personagem

# from Heroi import Heroi
from random import randint
from rich import print, inspect
from math import ceil
from funcs import gera_valor


class NPC(Personagem):
    def __init__(self, player_level, nome, raca, classe) -> None:
        super().__init__(nome, raca, classe)

        self.nivel = gera_valor(player_level)

        # if player_level > 1:
        #     self.nivel = randint(ceil(player_level * 0.5), int(player_level * 1.5))
        # else:
        #     self.nivel = 1

        self.hp_max = int(150 * player_level * randint(5, 15) / 10)
        self.hp = self.hp_max
        self.xp = randint(15, self.hp_max)
        self.vivo = True
        self.gold = randint(1, 100) * player_level
        # self.defesa = randint(ceil(player_level / 2), int(player_level * 2))
        self.defesa = randint(ceil(player_level / 2), player_level + 3)
        self.atk_arma = 15
        self.nome_item_usado_arma = "facao lixo"
        self.prob_especial_arma = 1
        self.tipo = "npc"

    def __str__(self):
        return f"""==============================
NPC FIAO

NOME: {self.nome}
RACA: {self.raca}
CLASSE: {self.classe}
NIVEL: {self.nivel}

VIVO: {self.esta_vivo()}
HP: {self.hp} / {self.hp_max}
XP: {self.xp}
GOLD: {self.gold}
MANA: {self.mana} / {self.mana_max}
"""
