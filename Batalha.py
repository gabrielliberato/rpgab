from Personagens import Personagem
from Heroi import Heroi
from NPC import NPC
from time import sleep
from rich import print
class Batalha:
    def __init__(self, jogador: Heroi, npc: NPC, verbose=False) -> None:
        self.jogador = jogador
        self.verbose = verbose
        self.npc = npc
        self.msg()
        self.finalizada = False

    def msg(self):
        if self.verbose: print(f"{self.jogador.nome} vs. {self.npc.nome}")

    def recupera_vida(self):
        self.jogador.set_hp(self.jogador.hp_max)
        self.npc.set_hp(self.npc.hp_max)
        self.jogador.revive()

    def inicia(self):

        self.jogador.prepara()
        # input("Começar partida? ")

        while self.jogador.hp > 0 and self.npc.hp > 0:
            print(f"\n{self.jogador.nome} ({self.jogador.hp}) x {self.npc.nome} ({self.npc.hp})")
            # sleep(1)
            self.jogador.atacar(self.npc)
            # print(f"{self.npc.nome}: {self.npc.hp}")
            self.npc.atacar(self.jogador)
            # print(f"{self.jogador.nome}: {self.jogador.hp}")
        self.finalizada = True
        self.analisa_vencedor()
        self.recupera_vida()

    def analisa_vencedor(self):
        if self.jogador.esta_vivo():
            print(f"{self.jogador.nome} venceu!!")
            self.jogador.add_xp(self.npc.xp)
            self.jogador.add_gold(self.npc.gold)
            self.jogador.add_vitoria()
            while self.jogador.xp >= self.jogador.xp_max:
                self.jogador.add_xp(-self.jogador.xp_max)
                self.jogador.upar()
        else:
            print(f"{self.npc.nome} venceu ):")
            self.jogador.add_derrota()
        self.jogador.heala()
    
    def venceu_batalha(self, inimigo: NPC):
        if self.get_tipo() == 'npc':
            if self.verbose: print("NPC ganhou fodasseeeee")
            inimigo.add_derrota()
            inimigo.add_partida()
        elif self.get_tipo() == 'eu':
            self.add_xp(inimigo.get_xp())
            self.add_gold(inimigo.gold)
            if self.verbose: print(f"Eu ganhei - XP: {self.get_xp()}")
            self.add_vitoria()
            self.add_partida()
            while self.get_xp() >= self.get_xp_max():
                self.add_xp(-self.get_xp_max())
                self.upar()
                # self.get_nivel() += 1
                self.add_xp_max(150)
                self.atk_arma = self.get_nivel() * 10
                self.atk_pet = self.get_nivel() * 3
                self.atk_magia = self.get_nivel() * 4
                self.def_magia = self.get_nivel() * 0
                self.set_xp_max(self.get_nivel() * 150 - 150)
