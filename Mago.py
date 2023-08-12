from Heroi import Heroi


class Mago(Heroi):

    # @staticmethod
    def usa_item(dici: dict, tipo: str) -> dict:
        for i in dici.values():
            if i["tipo"] == tipo:
                return i

    def __init__(self, nome, raca, classe) -> None:
        super().__init__(nome, raca, classe)

        self.inv_armas = {
            "bastao de mago": {
                "nivel": 1,
                "atk": 7,
                "def": 0,
                "especial": 2,
                "tipo": "earth",
            }
        }
        self.inv_escudos = {
            "escudo de lata": {
                "nivel": 1,
                "atk": 0,
                "def": 7,
                "especial": 0,
                "tipo": "earth",
            }
        }
        self.inv_armaduras = {
            "manto de malha": {
                "nivel": 1,
                "atk": 0,
                "def": 3,
                "especial": 0,
                "tipo": "earth",
            }
        }
        self.inv_pets = {"corvo": {"nivel": 1, "atk": 3, "def": 0, "especial": 80, "tipo": "darkness"}}
        self.inv_magias = {
            "fumaça": {
                "nivel": 1,
                "atk": 10,
                "def": 0,
                "especial": 10,
                "tipo": "wind",
                "preço": 20,
            }
        }
        self.inv_items = {"anel da sabedoria": {"nivel": 1, "atk": 3, "def": 0, "especial": 80, "tipo": "light"}}

        self.item_usado_arma = Mago.usa_item(self.inv_armas, "earth")
        self.atk_arma = self.item_usado_arma['atk']
        self.item_usado_escudo = Mago.usa_item(self.inv_escudos, "earth")
        self.def_escudo = self.item_usado_escudo['def']
        self.item_usado_armadura = Mago.usa_item(self.inv_armaduras, "earth")
        self.def_armadura = self.item_usado_armadura['def']
        self.item_usado_pet = Mago.usa_item(self.inv_pets, "darkness")
        self.atk_pet = self.item_usado_pet['def']
        self.item_usado_magia = Mago.usa_item(self.inv_magias, "wind")
        self.atk_magia = self.item_usado_magia['atk']
        self.def_magia = self.item_usado_magia['def']
        self.defesa = round(self.def_armadura * self.def_escudo, 2)
  
    def get_ataque(self):
        return self.atk_arma

    def get_defesa(self):
        return self.defesa
