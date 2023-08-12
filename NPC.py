from Personagens import Personagem
from random import randint

class NPC(Personagem):
    def __init__(self, player_level, nome, raca, classe) -> None:
        super().__init__(nome, raca, classe)
        
        if player_level > 1:
            self._info_nivel = randint(int(player_level * 0.5), int(player_level * 1.5))
        else:
            self._info_nivel = 1

        self._HP_MAX = 150 * player_level
        self._hp = self._HP_MAX
        self._xp = randint(15, self._HP_MAX) * 1 #player_level
        self._vivo = True
        self._gold = randint(1, 100) * player_level
        self._defesa = 10
        self._atk_arma = 10
        self._tipo = 'npc'

    @property
    def tipo(self):
        return self._tipo
    
    @property
    def defesa(self):
        return self._defesa
    
    @property
    def hp(self):
        return self._hp
    
    @property
    def atk_arma(self):
        return self._atk_arma

   
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
GOLD: {self._gold}
MANA: {self.mana} / {self.mana_max}
"""