import json
from player import Player

class HealthMonitor:
    health_records = {}  

    def __init__(self, player, injury_report):
        self.player = player  
        self.injury_report = injury_report
        HealthMonitor.health_records[player.name] = self 

    def update_info(self, injury_report):
        self.injury_report = injury_report
        HealthMonitor.save_to_json()

    def get_health_status(self):
        return self.injury_report

    def to_dici(self):
        return {
            "player_name": self.player.name,  
            "injury_report": self.injury_report
        }

    @classmethod
    def save_to_json(cls, filename="health_records.json"):
        with open(filename, "w") as file:
            json.dump([record.to_dict() for record in cls.health_records.values()], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="health_records.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.health_records = {}
                for item in data:
                    player = next((p for p in Player.players_list if p.name == item["player_name"]), None)
                    if player:
                        health_record = HealthMonitor(player, item["injury_report"])
                        cls.health_records[item["player_name"]] = health_record
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def __str__(self):
        return (
            f"Status de Saúde de {self.player.name}:\n"
            f"Relatório: {self.injury_report}\n"
        )