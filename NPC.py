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
        self.defesa = randint(ceil(player_level / 2), int(player_level * 2))
        self.atk_arma = 15
        self.nome_item_usado_arma = "facao lixo"
        self.tipo = 'npc'

    def atacar(self, eu):
        if eu.esta_vivo() and self.esta_vivo():
            dano = self.atk_arma - eu.defesa
            # print(self.atk_arma, eu.defesa)
            # dano = self.ataque

            # tratar o dano negativo enquanto não implemento tipos de ataque
            if dano <= 0:
                dano = 0
            
            if dano >= eu.hp: # hit kill
                dano = eu.hp
                eu.morre()
                # self.venceu_batalha(eu)
                # exit
            # print(f"\t - {self.nome.upper()} tirou {dano} de dano de {eu.nome.upper()}")
            print(f"\t- [r][b]{self.nome.upper()}[/b][/r] tirou [red b u]{dano}[/] de [r][b]{eu.nome.upper()}[/r][/b] usando [red b u]{self.nome_item_usado_arma}[/]")
            eu.toma_dano(dano)

   
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
