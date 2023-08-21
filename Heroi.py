from random import randint
from Personagens import Personagem
from NPC import NPC
from rich import print


class Heroi(Personagem):
    def __init__(self, nome, raca, classe):
        super().__init__(nome, raca, classe)

        self.stat_vitorias = 0
        self.stat_derrotas = 0
        self.stat_partidas_jogadas = 0
        self.gold = 0
        self.tipo = "eu"
        self.defesa = -666

        self.xp = 0
        self.xp_max = 150
        self.hp = 150
        self.hp_max = 150
        self.mana = 100
        self.mana_max = 100

        self.inv_armas = {}
        self.inv_escudos = {}
        self.inv_armaduras = {}
        self.inv_pets = {}
        self.inv_magias = {}
        self.inv_items = {}

    def add_vitoria(self):
        self.stat_vitorias += 1
        self.stat_partidas_jogadas += 1

    def add_derrota(self):
        self.stat_derrotas += 1
        self.stat_partidas_jogadas += 1

    def revive(self):
        self.vivo = True

    def add_xp(self, qtd):
        self.xp += qtd

    def add_xp_max(self, qtd):
        self.xp_max += qtd

    def set_xp_max(self, valor):
        self.xp_max = valor

    def set_hp_max(self, valor):
        self.hp_max = valor

    def add_gold(self, qtd):
        self.gold += qtd

    def __str__(self):
        return f"""
============================================================
NOME: {self.nome} ({self.stat_vitorias} / {self.stat_derrotas})
RACA: {self.raca}
CLASSE: {self.classe}
NIVEL: {self.nivel}

VIVO: {self.esta_vivo()}
HP: {self.hp} / {self.hp_max}
XP: {self.xp} / {self.xp_max}
MANA: {self.mana} / {self.mana_max}

"""

    def upar(self):
        print(f"UPOU DO NIVEL {self.nivel} para o {self.nivel+1}")
        self.nivel += 1
        self.xp_max += 150
        self.hp_max += 20
        self.mana_max += 25
        self.defesa += 100

    def prepara(self):
        op = 1
        op = 0

        while op in (1, 2, 3, 4, 5):
            op = int(
                input(
                    """
                           O que você deseja alterar?
1 - Magia
2 - Arma
3 - Escudo
4 - Armadura
5 - Pet
"""
                )
            )
            match op:
                case 1:
                    nomes_magias = self.inv_magias.keys()
                    print(len(nomes_magias), "magias\n")
                    if len(nomes_magias) == 1:
                        print("Voce nao consegue escolher pois só tem 1 magia")
                    else:
                        for indice, nome_magia in enumerate(nomes_magias):
                            print(
                                f"{indice}: {nome_magia} ({self.inv_magias[nome_magia]['tipo']})"
                            )
                        magia_escolhida = int(input("Escolha uma magia para equipar: "))
                        for indice, nome_magia in enumerate(nomes_magias):
                            print(indice)
                            if indice == magia_escolhida:
                                print("ACHEI A ARMA QUE VC QUER")
                                self.equipar_magia(magia_escolhida)
                                print(f"{self.nome_item_usado_magia} foi equipada!")
                                print(self)
                case 2:
                    nomes_armas = self.inv_armas.keys()
                    print(len(nomes_armas), "armas\n")
                    if len(nomes_armas) == 1:
                        print("Voce nao consegue escolher pois só tem 1 arma")
                    else:
                        for indice, nome_arma in enumerate(nomes_armas):
                            print(
                                f"{indice}: {nome_arma} ({self.inv_armas[nome_arma]['tipo']})"
                            )
                        arma_escolhida = int(input("Escolha uma arma para equipar: "))
                        for indice, nome_arma in enumerate(nomes_armas):
                            print(indice)
                            if indice == arma_escolhida:
                                print("ACHEI A ARMA QUE VC QUER")
                                self.equipar_arma(arma_escolhida)
                                print(f"{self.nome_item_usado_arma} foi equipada!")
                                print(self)

                case 3:
                    nomes_escudos = self.inv_escudos.keys()
                    if len(nomes_escudos) == 1:
                        print("Voce nao consegue escolher pois só tem 1 escudo")
                    else:
                        for p, i in enumerate(nomes_escudos):
                            print(f"{p}: {i} ({self.inv_escudos[i]['tipo']})")
                case 4:
                    nomes_armaduras = self.inv_armaduras.keys()
                    print(len(nomes_armaduras), "armaduras\n")
                    if len(nomes_armaduras) == 1:
                        print("Voce nao consegue escolher pois só tem 1 armadura")
                    else:
                        for indice, nome_armadura in enumerate(nomes_armaduras):
                            print(
                                f"{indice}: {nome_armadura} ({self.inv_armaduras[nome_armadura]['tipo']})"
                            )
                        armadura_escolhida = int(input("Escolha uma armadura para equipar: "))
                        for indice, nome_armadura in enumerate(nomes_armaduras):
                            print(indice)
                            if indice == armadura_escolhida:
                                print("ACHEI A ARMA QUE VC QUER")
                                self.equipar_armadura(armadura_escolhida)
                                print(f"{self.nome_item_usado_armadura} foi equipada!")
                                print(self)
                case 5:
                    nomes_pets = self.inv_pets.keys()
                    if len(nomes_pets) == 1:
                        print("Voce nao consegue escolher pois só tem 1 pet")
                    else:
                        for p, i in enumerate(nomes_pets):
                            print(f"{p}: {i} ({self.inv_pets[i]['tipo']})")

    def usa_item(inventario: dict, tipo: str) -> dict:
        for i in inventario.values():
            if i["tipo"] == tipo:
                return i
