from Personagens import Personagem
from time import sleep

class Batalha:
    def __init__(self, jogador: Personagem, npc: Personagem, verbose=False) -> None:
        self.jogador = jogador
        self._verbose = verbose
        self.npc = npc
        self.msg()
        self.finalizada = False

    def msg(self):
        if self._verbose: print(f"{self.jogador.nome} vs. {self.npc.nome}")

    def recupera_vida(self):
        self.jogador.set_hp(self.jogador.get_hp_max())
        self.npc.set_hp(self.npc.get_hp_max())
        self.jogador.revive()        
        self.npc.revive()

    def inicia(self):
        while self.jogador.get_hp() > 0 and self.npc.get_hp() > 0:
            # sleep(1)
            self.jogador.atacar(self.npc)
            # print(f"{self.npc.nome}: {self.npc.hp}")
            # sleep(1)
            self.npc.atacar(self.jogador)
            # print(f"{self.jogador.nome}: {self.jogador.hp}")
            # print(f"{self.jogador.get_nome()} ({self.jogador.get_hp()}) x {self.npc.get_nome()} ({self.npc.get_hp()})")
        self.finalizada = True
        if self._verbose:
            # print(self.jogador.get_nivel(), " -> ", self.jogador.get_xp())
            pass
        self.recupera_vida()

    def venceu_batalha(self, inimigo: 'Personagem'):
        if self.get_tipo() == 'npc':
            if self._verbose: print("NPC ganhou fodasseeeee")
            inimigo.add_derrota()
            inimigo.add_partida()
        elif self.get_tipo() == 'eu':
            self.add_xp(inimigo.get_xp())
            if self._verbose: print(f"Eu ganhei - XP: {self.get_xp()}")
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
