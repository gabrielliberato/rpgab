from random import randint
from rich import print, inspect
import os
import csv


class Personagem:
    def __init__(self, nome, raca, classe):
        self._info_nome = nome
        self._info_raca = raca
        self._info_classe = classe
        self._info_nivel = 1
        self._tipo = 'eu'

        self.vivo = True

        self._xp = 0
        self._XP_MAX = 150
        self._hp = 150
        self._HP_MAX = 150
        self._mana = 100
        self._MANA_MAX = 100

    def __str__(self):
        return f"""
NOME: {self.nome}
RACA: {self.raca}
CLASSE: {self.classe}
NIVEL: {self.nivel}

VIVO: {self.esta_vivo()}
HP: {self.hp} / {self.hp_max}
XP: {self.xp} / {self.xp_max}
MANA: {self.mana} / {self.mana_max}
"""

    @property
    def tipo(self):
        return self._tipo
    
    @property
    def nome(self):
        return self._info_nome

    @property
    def raca(self):
        return self._info_raca

    @property
    def classe(self):
        return self._info_classe

    @property
    def nivel(self):
        return self._info_nivel
    
    def esta_vivo(self):
        return self.vivo
    
    @property
    def hp(self):
        return self._hp

    @property
    def hp_max(self):
        return self._HP_MAX

    @property
    def xp(self):
        return self._xp

    @property
    def xp_max(self):
        return self._XP_MAX
    
    @property
    def mana(self):
        return self._mana

    def set_hp(self, valor):
        self._hp = valor
    
    @property
    def mana_max(self):
        return self._MANA_MAX
    
    # Métodos em combate    

    def morre(self):
        self.vivo = False

    def heala(self, qtd=None):
        if qtd is None:
            self._hp = self._HP_MAX
        else:
            self._hp = qtd

    def toma_dano(self, dano):
        self._hp -= dano

    def __forca_ataque(self, level: int):
        forca = 1 * level
        return forca

    def upar(self):
        print(f"UPOU DO NIVEL {self._info_nivel} para o {self._info_nivel+1}")
        self._info_nivel += 1
        self._XP_MAX += 150
        self.atk_arma = self.nivel * 10
        self.atk_pet = self.nivel * 3
        self.atk_magia = self.nivel * 4
        self.def_magia = self.nivel * 0

    def venceu_batalha(self, inimigo: 'Personagem'):
        if self.tipo == 'npc':
            inimigo.add_derrota()
            inimigo.add_partida()
        elif self.tipo == 'eu':
            self.add_xp(inimigo.xp)
            self.add_vitoria()
            self.add_partida()
            while self.xp >= self.xp_max:
                self.add_xp(-self.xp_max)
                self.upar()

    
    def atacar(self, inimigo: "Personagem"):
        # print(f"{self.nome} está atacando {inimigo.nome}")
        if inimigo.esta_vivo() and self.esta_vivo():
            dano = round(self.nivel * self.atk_arma * inimigo.defesa)
            # dano = self.ataque

            # tratar o dano negativo enquanto não implemento tipos de ataque
            if dano < 0:
                dano = 0

            if dano >= inimigo.hp: # hit kill
                dano = inimigo.hp
                inimigo.morre()
                self.venceu_batalha(inimigo)
                # exit
            print(dano)
            # print(f"[r][b]{self._info_nome.upper()}[/b][/r] tirou [red b u]{dano}[/] de [r][b]{inimigo.nome.upper()}[/r][/b] usando [red b u]{self.item_arma}[/]")
            inimigo.toma_dano(dano)
            # print(f"{inimigo.nome.upper()} ficou com {inimigo.hp} de vida!")

            # print(f"{self._info_nome} não pode atacar pois {inimigo.nome} já está morto.")
            # exit

    def instance_attributes(self):
        return [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]

    def append_to_csv(self, filename="docs/chars.csv"):
        file_exists = os.path.exists(filename)
        instance_attributes = self.instance_attributes

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