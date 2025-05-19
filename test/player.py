import json

class Player:
    players_list = []

    def __init__(self, name, age, height, weight, position):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        Player.players_list.append(self)

    # Creational Pattern: Factory Method
    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("name", "Desconhecido"),
            data.get("age", 0),
            data.get("height", 0.0),
            data.get("weight", 0.0),
            data.get("position", "Desconhecida")
        )

    @classmethod
    def save_to_json(cls, filename="players.json"):
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="players.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = []
                for player_data in data:
                    player = cls.from_dict(player_data)
                    cls.players_list.append(player)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "position": self.position
        }

    @classmethod
    def carregar_dados(cls):
        cls.load_from_json()

    @classmethod
    def salvar_dados(cls):
        cls.save_to_json()

    # Behavioral Pattern: Command-style update method
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return (
            f" Jogador: {self.name}\n"
            f" Idade: {self.age}\n"
            f" Altura: {self.height}\n"
            f" Peso: {self.weight}\n"
            f" Posição: {self.position}\n"
        )

# Structural Pattern: Decorator
class PlayerDecorator:
    def __init__(self, player):
        self._player = player

    def __getattr__(self, attr):
        return getattr(self._player, attr)

    def display_with_title(self):
        return f"*** Jogador Destaque ***\n{self._player}"
