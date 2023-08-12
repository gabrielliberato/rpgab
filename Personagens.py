from random import randint
from rich import print, inspect
import os
import csv


class Personagem:
    def __init__(self, nome, raca, classe):
        self.info_nome = nome
        self.info_raca = raca
        self.info_classe = classe
        self.info_nivel = 1

        self.vivo = True

        self.xp = 0
        self.XP_MAX = 150
        self.hp = 150
        self.HP_MAX = 150
        self.mana = 100
        self.MANA_MAX = 100

    def __str__(self):
        return f"""
NOME: {self.get_nome()}
RACA: {self.get_raca()}
CLASSE: {self.get_classe()}
NIVEL: {self.get_nivel()}

VIVO: {self.esta_vivo()}
HP: {self.get_hp()} / {self.get_hp_max()}
XP: {self.get_xp()} / {self.get_xp_max()}
MANA: {self.get_mana()} / {self.get_mana_max()}
"""

    def get_nome(self):
        return self.info_nome

    def get_raca(self):
        return self.info_raca

    def get_classe(self):
        return self.info_classe

    def get_nivel(self):
        return self.info_nivel
    
    def esta_vivo(self):
        return self.vivo
    
    def get_hp(self):
        return self.hp

    def get_hp_max(self):
        return self.HP_MAX

    def get_xp(self):
        return self.xp

    def get_xp_max(self):
        return self.XP_MAX
    
    def get_mana(self):
        return self.mana

    def set_hp(self, valor):
        self.hp = valor
    
    def get_mana_max(self):
        return self.MANA_MAX
    
    # Métodos em combate    

    def morre(self):
        self.vivo = False

    def heala(self, qtd=None):
        if qtd is None:
            self.hp = self.HP_MAX
        else:
            self.hp = qtd

    def toma_dano(self, dano):
        self.hp -= dano

    def __forca_ataque(self, level: int):
        forca = 1 * level
        return forca

    def upar(self):
        self.info_nivel += 1

    def atacar(self, inimigo: "Personagem"):
        # print(f"{self.get_nome()} está atacando {inimigo.get_nome()}")
        if inimigo.esta_vivo() and self.esta_vivo():
            dano = round(self.get_nivel() * self.atk_arma * inimigo.defesa)
            # dano = self.ataque

            # tratar o dano negativo enquanto não implemento tipos de ataque
            if dano < 0:
                dano = 0

            if dano >= inimigo.get_hp():
                dano = inimigo.get_hp()
                inimigo.morre()
                self.venceu_batalha(inimigo)
                # exit
            # print(dano)
            # print(f"[r][b]{self.info_nome.upper()}[/b][/r] tirou [red b u]{dano}[/] de [r][b]{inimigo.nome.upper()}[/r][/b] usando [red b u]{self.item_arma}[/]")
            inimigo.toma_dano(dano)
            # print(f"{inimigo.nome.upper()} ficou com {inimigo.hp} de vida!")

            # print(f"{self.info_nome} não pode atacar pois {inimigo.nome} já está morto.")
            # exit

    def get_instance_attributes(self):
        return [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]

    def append_to_csv(self, filename="docs/chars.csv"):
        file_exists = os.path.exists(filename)
        instance_attributes = self.get_instance_attributes()

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:  # If file doesn't exist, write header
                writer.writerow(instance_attributes)

            writer.writerow([getattr(self, attr) for attr in instance_attributes])

    # @classmethod
    # def gera_personagem(cls, params):
    #     perso = Personagem(params['nome'], params['raca'], params['classe'], params['tipo'])

    #     perso. {'nome': params['nome'],
    #         'raca': params['raca'],
    #         'classe': params['classe'],
    #         'tipo': params['tipo']
    #     }

    #     perso. {           'nivel': params['nivel'],
    #         'xp': params['xp'],
    #         'XP_MAX': params['XP_MAX'],
    #         'hp': params['hp'],
    #         'HP_MAX': params['HP_MAX'],
    #         'vivo': params['vivo']
    #     }

    #     perso. {           'vitorias': params['vitorias'],
    #         'derrotas': params['derrotas'],
    #         'partidas_jogadas': params['partidas_jogadas']
    #     }

    #     perso._verbose = params['_verbose']

    #     perso. {           'arma_empunhada': params['item_arma'],
    #         'atk_arma': params['atk_arma'],
    #         'item_escudo': params['item_escudo'],
    #         'def_escudo': params['def_escudo'],
    #         'item_armadura': params['item_armadura'],
    #         'def_armadura': params['def_armadura'],
    #         'item_pet': params['item_pet'],
    #         'atk_pet': params['atk_pet'],
    #         'magia': params['magia'],
    #         'atk_magia': params['atk_magia'],
    #         'def_magia': params['def_magia'],
    #         'defesa': params['defesa']
    #     }

    #     return perso

    # @classmethod
    # def load_from_csv(cls, filename, character_name):
    #     import pandas as pd

    #     chars = pd.read_csv(filename)
    #     char = chars[chars['nome'] == character_name]

    #     parametros = char.to_dict('records')[0]

    #     return cls.gera_personagem(parametros)


class NPC(Personagem):
    def __init__(self, player_level, nome, raca, classe, tipo) -> None:
        print("oi")
        super().__init__(nome, raca, classe, tipo)
        if player_level > 1:
            self.info_nivel = randint(int(player_level * 0.5), int(player_level * 1.5))
        else:
            self.info_nivel = 1

        self.xp = 10
        self.XP_MAX = 150
        self.hp = 150
        self.HP_MAX = 150
        self.vivo = True

    def __str__(self) -> str:
        return super().__str__() + "NPC FIÃO"