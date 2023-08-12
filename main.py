from Personagens import Personagem, NPC
from Heroi import Heroi
from Mago import Mago
from Batalha import *

from math import floor
from rich import inspect

p = Mago('gab', 'mago', 'arqueiro')
p2 = Personagem('memis', 'mago', 'arqueiro')
inspect(p2)
print(p2)


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