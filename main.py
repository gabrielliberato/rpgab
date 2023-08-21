from NPC import NPC
from Heroi import Heroi
from Mago import Mago
from Batalha import *

from math import floor
from rich import inspect, print

p = Mago('gab', 'mago', 'arqueiro')
for _ in range(20):
    npc = NPC(p.nivel, 'npccc', 'memeiro', 'tunado')
    print(f"O NPC VAI DAR {npc.xp}\n")
    # print(p)
    b = Batalha(p, npc)
    b.inicia()
    print(p)
#     inspect(p)
    # input()



# npc = NPC(p.get_nivel(), 'ini', 'raca', 'classsse', 'npc')

# # inspect(p)

# for _ in range(500):
#     b = Batalha(p, npc)
#     b.inicia()
#     b.recupera_vida()

# inspect(p)
# inspect(npc)

# p.append_to_csv('docs/chars.csv')

# character_name = 'gab'
# loaded_character = Personagem.load_from_csv(r'C:\Users\Gabriel\Documents\Projetos Python\rpgab\docs\chars.csv', character_name)
# print(loaded_character)

# for _ in range(5000):
#     b = Batalha(loaded_character, i)
#     b.inicia()
#     b.recupera_vida()

# inspect(loaded_character)