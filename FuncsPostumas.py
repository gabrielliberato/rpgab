
    # def instance_attributes(self):
    #     return [
    #         attr
    #         for attr in dir(self)
    #         if not callable(getattr(self, attr)) and not attr.startswith("__")
    #     ]

    # def append_to_csv(self, filename="docs/chars.csv"):
    #     file_exists = os.path.exists(filename)
    #     instance_attributes = self.instance_attributes

    #     with open(filename, mode="a", newline="") as file:
    #         writer = csv.writer(file)

    #         if not file_exists:  # If file doesn't exist, write header
    #             writer.writerow(instance_attributes)

    #         writer.writerow([getattr(self, attr) for attr in instance_attributes])

    # # @classmethod
    # # def gera_personagem(cls, params):
    # #     perso = Personagem(params['nome'], params['raca'], params['classe'], params['tipo'])

    # #     perso. {'nome': params['nome'],
    # #         'raca': params['raca'],
    # #         'classe': params['classe'],
    # #         'tipo': params['tipo']
    # #     }

    # #     perso. {           'nivel': params['nivel'],
    # #         'xp': params['xp'],
    # #         'XP_MAX': params['XP_MAX'],
    # #         'hp': params['hp'],
    # #         'HP_MAX': params['HP_MAX'],
    # #         'vivo': params['vivo']
    # #     }

    # #     perso. {           'vitorias': params['vitorias'],
    # #         'derrotas': params['derrotas'],
    # #         'partidas_jogadas': params['partidas_jogadas']
    # #     }

    # #     perso._verbose = params['_verbose']

    # #     perso. {           'arma_empunhada': params['item_arma'],
    # #         'atk_arma': params['atk_arma'],
    # #         'item_escudo': params['item_escudo'],
    # #         'def_escudo': params['def_escudo'],
    # #         'item_armadura': params['item_armadura'],
    # #         'def_armadura': params['def_armadura'],
    # #         'item_pet': params['item_pet'],
    # #         'atk_pet': params['atk_pet'],
    # #         'magia': params['magia'],
    # #         'atk_magia': params['atk_magia'],
    # #         'def_magia': params['def_magia'],
    # #         'defesa': params['defesa']
    # #     }

    # #     return perso

    # # @classmethod
    # # def load_from_csv(cls, filename, character_name):
    # #     import pandas as pd

    # #     chars = pd.read_csv(filename)
    # #     char = chars[chars['nome'] == character_name]

    # #     parametros = char.to_dict('records')[0]

    # #     return cls.gera_personagem(parametros)