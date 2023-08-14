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
        self.tipo = 'eu'
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
        self.xp_max + qtd

    def set_xp_max(self, valor):
        self.xp_max = valor

    def set_hp_max(self, valor):
        self.hp_max = valor

    def add_gold(self, qtd):
        self.gold += qtd

    # def venceu_batalha(self, inimigo: NPC):
    #     if self.tipo == 'npc':
    #         inimigo.add_derrota()
    #         inimigo.add_partida()
    #     elif self.tipo == 'eu':
    #         self.add_xp(inimigo.xp)
    #         self.add_vitoria()
    #         self.add_partida()
    #         while self.xp >= self.xp_max:
    #             self.add_xp(-self.xp_max)
    #             # self.add
    #             self.upar()

    def __str__(self):
        return f"""
============================================================
NOME: {self.nome}
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
        self.defesa += 1

    def prepara(self):
        op = 1

        while op in (1, 2, 3, 4, 5):
            op = int(input("""
                           O que você deseja alterar?
1 - Magia
2 - Arma
3 - Escudo
4 - Armadura
5 - Pet
"""))
            match op:
                case 1:
                    nomes_magias = self.inv_magias.keys()
                    if len(nomes_magias) == 1:
                        print("Voce nao consegue escolher pois só tem 1 magia")
                    else:
                        for p, i in enumerate(nomes_magias):
                            print(f"{p}: {i} ({self.inv_magias[i]['tipo']})")
                case 2:
                    nomes_armas = self.inv_armas.keys()
                    if len(nomes_armas) == 1:
                        print("Voce nao consegue escolher pois só tem 1 arma")
                    else:
                        for p, i in enumerate(nomes_armas):
                            print(f"{p}: {i} ({self.inv_armas[i]['tipo']})")
                        arma_escolhida = int(input("Escolha uma arma para equipar: "))
                        for p, i in enumerate(nomes_armas):
                            if p == arma_escolhida:
                                self.item_usado_arma = Heroi.usa_item(self.inv_armas, {self.inv_armas[i]['tipo']})
                                self.nome_item_usado_arma = list(self.inv_armas.keys())[p] # TODO: CRIAR METODO PRA SUBSTITUIR ESSAS LINHAS
                                self.atk_arma = self.item_usado_arma['atk']

                case 3:
                    nomes_escudos = self.inv_escudos.keys()
                    if len(nomes_escudos) == 1:
                        print("Voce nao consegue escolher pois só tem 1 escudo")
                    else:
                        for p, i in enumerate(nomes_escudos):
                            print(f"{p}: {i} ({self.inv_escudos[i]['tipo']})")
                case 4:
                    nomes_armaduras = self.inv_armaduras.keys()
                    if len(nomes_armaduras) == 1:
                        print("Voce nao consegue escolher pois só tem 1 armadura")
                    else:
                        for p, i in enumerate(nomes_armaduras):
                            print(f"{p}: {i} ({self.inv_armaduras[i]['tipo']})")
                case 5:
                    nomes_pets = self.inv_pets.keys()
                    if len(nomes_pets) == 1:
                        print("Voce nao consegue escolher pois só tem 1 pet")
                    else:
                        for p, i in enumerate(nomes_pets):
                            print(f"{p}: {i} ({self.inv_pets[i]['tipo']})")

    def usa_item(dici: dict, tipo: str) -> dict:
        for i in dici.values():
            if i["tipo"] == tipo:
                return i