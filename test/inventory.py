import uuid
import json

class Inventory:
    _inventory = {}  

    def __init__(self, type_object, sector, team, registration_year, last_use_date):
        self._id = str(uuid.uuid4())[:8]  
        self._type_object = type_object
        self._sector = sector
        self._team = team
        self._registration_year = registration_year
        self._last_use_date = last_use_date
        self._available = True
        Inventory._inventory[self._id] = self
        Inventory.save_to_json()

    # Getters e Setters
    @property
    def id(self):
        return self._id

    @property
    def type_object(self):
        return self._type_object

    @type_object.setter
    def type_object(self, value):
        self._type_object = value
        Inventory.save_to_json()

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, value):
        self._sector = value
        Inventory.save_to_json()

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value
        Inventory.save_to_json()

    @property
    def registration_year(self):
        return self._registration_year

    @registration_year.setter
    def registration_year(self, value):
        self._registration_year = value
        Inventory.save_to_json()

    @property
    def last_use_date(self):
        return self._last_use_date

    @last_use_date.setter
    def last_use_date(self, value):
        self._last_use_date = value
        Inventory.save_to_json()

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
        Inventory.save_to_json()

    def toggle_availability(self):
        self._available = not self._available
        Inventory.save_to_json()
        return f"Disponibilidade de {self._type_object} alterada para {self._available}."

    def to_dict(self):
        return {
            "id": self._id,
            "type_object": self._type_object,
            "sector": self._sector,
            "team": self._team,
            "registration_year": self._registration_year,
            "last_use_date": self._last_use_date,
            "available": self._available
        }

    @classmethod
    def save_to_json(cls, filename="inventory.json"):
        with open(filename, "w") as file:
            json.dump([item.to_dict() for item in cls._inventory.values()], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="inventory.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._inventory = {}
                for item in data:
                    loaded_item = Inventory(
                        item["type_object"],
                        item["sector"],
                        item["team"],
                        item["registration_year"],
                        item["last_use_date"]
                    )
                    loaded_item._id = item["id"]
                    loaded_item._available = item["available"]
                    cls._inventory[item["id"]] = loaded_item
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def __str__(self):
        return (
            f" ID: {self._id} | Objeto: {self._type_object}\n"
            f" Setor: {self._sector} | Equipe: {self._team}\n"
            f" Ano de Registro: {self._registration_year} | Último Uso: {self._last_use_date}\n"
            f" Status: {'Disponível' if self._available else 'Indisponível'}"
        )

    @classmethod
    def get_equipment_by_id(cls, equipment_id):
        return cls._inventory.get(equipment_id)