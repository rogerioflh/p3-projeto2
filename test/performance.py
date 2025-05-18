import json
from player import Player

class Performance:
    performance_data = {}  

    def __init__(self, player, passes, goals, assists, defenses, meters):
        self.player = player  
        self.passes = passes
        self.goals = goals
        self.assists = assists
        self.defenses = defenses
        self.meters = meters
        Performance.performance_data[player.name] = self  

    def update_info(self, passes=None, goals=None, assists=None, defenses=None, meters=None):
        if passes is not None:
            self.passes = passes
        if goals is not None:
            self.goals = goals
        if assists is not None:
            self.assists = assists
        if defenses is not None:
            self.defenses = defenses
        if meters is not None:
            self.meters = meters
        Performance.save_to_json()

    def to_dict(self):
        return {
            "player_name": self.player.name,  
            "passes": self.passes,
            "goals": self.goals,
            "assists": self.assists,
            "defenses": self.defenses,
            "meters": self.meters
        }

    @classmethod
    def save_to_json(cls, filename="performance_data.json"):
        with open(filename, "w") as file:
            json.dump([record.to_dict() for record in cls.performance_data.values()], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="performance_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.performance_data = {}
                for item in data:
                    player = next((p for p in Player.players_list if p.name == item["player_name"]), None)
                    if player:
                        performance_record = Performance(
                            player,
                            item["passes"],
                            item["goals"],
                            item["assists"],
                            item["defenses"],
                            item["meters"]
                        )
                        cls.performance_data[item["player_name"]] = performance_record
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def __str__(self):
        return (
            f"Desempenho de {self.player.name}:\n"
            f"Passes: {self.passes}\n"
            f"Gols: {self.goals}\n"
            f"Assistências: {self.assists}\n"
            f"Defesas: {self.defenses}\n"
            f"Metros percorridos: {self.meters}\n"
        )
        