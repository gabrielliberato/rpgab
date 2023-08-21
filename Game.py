from NPC import NPC
from Heroi import Heroi
from Mago import Mago
from Batalha import *

from math import floor
from rich import inspect, print

class Game:
    @staticmethod
    def run():
        op = 1
        while op != 3:
            op = int(input("""
======================
        RPGAB
======================
1 - JOGAR
2 - LOJA
3 - SAIR
    """))
            
            match op:
                case 1:
                    print("jogando")
                    p = Mago('gab', 'mago', 'arqueiro')
                    for _ in range(20):
                        npc = NPC(p.nivel, 'npccc', 'memeiro', 'tunado')
                        print(f"O NPC VAI DAR {npc.xp}\n")
                        print(p)
                        b = Batalha(p, npc)
                        b.inicia()
                        print(p)
                        inspect(p)
                        # input()
                case 2:
                    print("lojinha")
                case 3:
                    print("saindo flws")
            
Game.run()