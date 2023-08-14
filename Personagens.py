from random import randint
from rich import print, inspect
import os
import csv


class Personagem:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.tipo = "eu"

        self.vivo = True

        self.xp = -666
        self.hp = -666
        self.hp_max = -666
        self.mana = -666
        self.mana_max = -666

    

    def esta_vivo(self):
        return self.vivo

    def set_hp(self, valor):
        self.hp = valor

    # Métodos em combate

    def morre(self):
        self.vivo = False

    def heala(self, qtd=None):
        if qtd is None:
            self.hp = self.hp_max
        else:
            self.hp = qtd

    def toma_dano(self, dano):
        self.hp -= dano

    def atacar(self, inimigo: "Personagem"):
        # print(f"{self.nome} está atacando {inimigo.nome}")
        if inimigo.esta_vivo() and self.esta_vivo():
            dano = round(self.atk_arma - inimigo.defesa)
            # dano = self.ataque

            # tratar o dano negativo enquanto não implemento tipos de ataque
            if dano < 0:
                dano = 0

            if dano >= inimigo.hp:  # hit kill
                dano = inimigo.hp
                inimigo.morre()
                # self.venceu_batalha(inimigo)
                # exit
            # print(f"\t - {self.nome.upper()} tirou {dano} de dano de {inimigo.nome.upper()}")
            print(
                f"\t- [r][b]{self.nome.upper()}[/b][/r] tirou [red b u]{dano}[/] de [r][b]{inimigo.nome.upper()}[/r][/b] usando [red b u]{self.nome_item_usado_arma}[/]"
            )
            inimigo.toma_dano(dano)
            # print(f"{inimigo.nome.upper()} ficou com {inimigo.hp} de vida!")

            # print(f"{self.nome} não pode atacar pois {inimigo.nome} já está morto.")
            # exit
        else:
            print("Ninguém pode atacar porque um jogador já morreu")
            pass
