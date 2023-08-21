from Heroi import Heroi
from rich import print


class Mago(Heroi):
    # @staticmethod
    def usa_item(self, dici: dict, tipo: str) -> dict:
        for i in dici.values():
            print(f"==== {i}")
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
            },
            "varinha": {
                "nivel": 1,
                "atk": 6,
                "def": 1,
                "especial": 2,
                "tipo": "energy",
            },
        }
        self.set_qtd_armas()

        self.inv_escudos = {
            "escudo de lata": {
                "nivel": 1,
                "atk": 0,
                "def": 7,
                "especial": 0,
                "tipo": "earth",
            }
        }
        self.set_qtd_escudos()
        
        self.inv_armaduras = {
            "manto de malha": {
                "nivel": 1,
                "atk": 0,
                "def": 3,
                "especial": 0,
                "tipo": "earth",
            },
            "armadura de guerreiro": {
                "nivel": 1,
                "atk": 0,
                "def": 40,
                "especial": 0,
                "tipo": "wind",
            },
        }
        self.set_qtd_armaduras()
        
        self.inv_pets = {
            "corvo": {
                "nivel": 1,
                "atk": 3,
                "def": 0,
                "especial": 80,
                "tipo": "darkness",
            }
        }
        self.set_qtd_pets()
        
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
        self.set_qtd_magias()
        
        self.inv_items = {
            "anel da sabedoria": {
                "nivel": 1,
                "atk": 3,
                "def": 0,
                "especial": 80,
                "tipo": "light",
            }
        }
        self.set_qtd_items()

        self.item_usado_arma = self.usa_item(self.inv_armas, "earth")
        self.nome_item_usado_arma = list(self.inv_armas.keys())[0]
        self.atk_arma = self.item_usado_arma["atk"]
        self.def_arma = self.item_usado_arma["def"]
        self.prob_especial_arma = self.item_usado_arma["especial"]

        self.item_usado_escudo = self.usa_item(self.inv_escudos, "earth")
        self.nome_item_usado_escudo = list(self.inv_escudos.keys())[0]
        self.atk_escudo = self.item_usado_escudo["atk"]
        self.def_escudo = self.item_usado_escudo["def"]

        self.item_usado_armadura = self.usa_item(self.inv_armaduras, "earth")
        self.nome_item_usado_armadura = list(self.inv_armaduras.keys())[0]
        self.atk_armadura = self.item_usado_armadura["atk"]
        self.def_armadura = self.item_usado_armadura["def"]

        self.item_usado_pet = self.usa_item(self.inv_pets, "darkness")
        self.nome_item_usado_pet = list(self.inv_pets.keys())[0]
        self.atk_pet = self.item_usado_pet["atk"]
        self.def_pet = self.item_usado_pet["def"]

        self.item_usado_magia = self.usa_item(self.inv_magias, "wind")
        self.nome_item_usado_magia = list(self.inv_magias.keys())[0]
        self.atk_magia = self.item_usado_magia["atk"]
        self.def_magia = self.item_usado_magia["def"]

        self.set_defesa()

    def set_qtd_armas(self):
        self.qtd_armas = len(self.inv_armas.keys())

    def set_qtd_armaduras(self):
        self.qtd_armaduras = len(self.inv_armaduras.keys())

    def set_qtd_escudos(self):
        self.qtd_escudos = len(self.inv_escudos.keys())

    def set_qtd_pets(self):
        self.qtd_pets = len(self.inv_pets.keys())

    def set_qtd_magias(self):
        self.qtd_magias = len(self.inv_magias.keys())

    def set_qtd_items(self):
        self.qtd_items = len(self.inv_items.keys())

    def set_defesa(self):
        self.defesa = self.def_armadura + self.def_escudo

    def set_atribs_dep_arma(self, indice):
        self.nome_item_usado_arma = list(self.inv_armas.keys())[indice]
        self.atk_arma = self.item_usado_arma["atk"]
        self.def_arma = self.item_usado_arma["def"]
        self.set_defesa()

    def set_atribs_dep_armadura(self, indice):
        self.nome_item_usado_armadura = list(self.inv_armaduras.keys())[indice]
        self.atk_armadura = self.item_usado_armadura["atk"]
        self.def_armadura = self.item_usado_armadura["def"]
        self.set_defesa()

    def set_atribs_dep_escudo(self, indice):
        self.nome_item_usado_escudo = list(self.inv_escudos.keys())[indice]
        self.atk_escudo = self.item_usado_escudo["atk"]
        self.def_escudo = self.item_usado_escudo["def"]
        self.set_defesa()

    def set_atribs_dep_pet(self, indice):
        self.nome_item_usado_pet = list(self.inv_pets.keys())[indice]
        self.atk_pet = self.item_usado_pet["atk"]
        self.def_pet = self.item_usado_pet["def"]
        self.set_defesa()

    def set_atribs_dep_pet(self, indice):
        self.nome_item_usado_magia = list(self.inv_magias.keys())[indice]
        self.atk_magia = self.item_usado_magia["atk"]
        self.def_magia = self.item_usado_magia["def"]
        self.set_defesa()

    def equipar_arma(self, indice_arma):
        if indice_arma > self.qtd_armas:
            raise IndexError("Essa arma não existe")

        nomes_armas = self.inv_armas.keys()
        for i, nome_arma in enumerate(nomes_armas):
            print(i)
            if i == indice_arma:
                self.item_usado_arma = Heroi.usa_item(
                    inventario=self.inv_armas, tipo=self.inv_armas[nome_arma]["tipo"]
                )
                self.set_atribs_dep_arma(indice=i)

    def equipar_armadura(self, indice_armadura):
        if indice_armadura > self.qtd_armaduras:
            raise IndexError("Essa armadura não existe")

        nomes_armaduras = self.inv_armaduras.keys()
        for i, nome_armadura in enumerate(nomes_armaduras):
            print(i)
            if i == indice_armadura:
                self.item_usado_armadura = Heroi.usa_item(
                    inventario=self.inv_armaduras,
                    tipo=self.inv_armaduras[nome_armadura]["tipo"],
                )
                self.set_atribs_dep_armadura(indice=i)

    def get_ataque(self):
        return self.atk_arma

    def get_defesa(self):
        return self.defesa

    def __str__(self):
        return (
            super().__str__()
            + f"""
ARMA: {self.nome_item_usado_arma} ({self.atk_arma} ATK) - [{self.item_usado_arma["tipo"].upper()}]
ARMADURA: {self.nome_item_usado_armadura} ({self.def_armadura} DEF) - [{self.item_usado_armadura["tipo"].upper()}]
ESCUDO: {self.nome_item_usado_escudo} ({self.def_escudo} DEF) - [{self.item_usado_escudo["tipo"].upper()}]
PET: {self.nome_item_usado_pet} ({self.atk_pet} ATK) - [{self.item_usado_pet["tipo"].upper()}]
MAGIA: {self.nome_item_usado_magia} ({self.atk_magia} ATK / {self.def_magia} DEF) - [{self.item_usado_magia["tipo"].upper()}]

DEFESA: {self.defesa}
GOLD: {self.gold}
============================================================\n"""
        )
