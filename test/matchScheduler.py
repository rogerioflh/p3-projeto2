import json
from event import Event
import datetime

class MatchScheduler(Event):
    competitions_list = []

    def __init__(self, type, location, date, time, opponent):
        super().__init__(type, date, time, location)
        self.__opponent = opponent
        self.__status = False
        MatchScheduler.competitions_list.append(self)
        MatchScheduler.save_to_json()

    # Getters
    def get_opponent(self):
        return self.__opponent
    
    def get_status(self):
        return self.__status
    
    # Setters
    def set_opponent(self, opponent):
        self.__opponent = opponent
    
    def set_status(self, status):
        self.__status = status
    
    def schedule_match(self):
        return f"Partida agendada: {self.get_type()} contra {self.__opponent} em {self.get_location()}, no dia {self.get_date()} às {self.get_time()}."

    def mark_as_completed(self):
        self.__status = True
        MatchScheduler.save_to_json()
        return f"Partida {self.get_type()} contra {self.__opponent} marcada como concluída."

    def mark_as_not_completed(self):
        self.__status = False
        MatchScheduler.save_to_json()
        return f"Partida {self.get_type()} contra {self.__opponent} marcada como não concluída."

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.get_date()} {self.get_time()}", "%d/%m/%Y %H:%M")
            if datetime_evento < datetime.now():
                return "A partida já ocorreu."
            else:
                return "A partida ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    @classmethod
    def save_to_json(cls, filename="matches.json"):
        with open(filename, "w") as file:
            json.dump([match.to_dict() for match in cls.competitions_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="matches.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.competitions_list = []
                for item in data:
                    match = MatchScheduler(
                        item["type"],
                        item["location"],
                        item["date"],
                        item["time"],
                        item["opponent"]
                    )
                    match.__status = item.get("status", False)
                    cls.competitions_list.append(match)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        event_dict = super().to_dict()
        event_dict["opponent"] = self.__opponent
        event_dict["status"] = self.__status
        return event_dict

    def __str__(self):
        status_text = "Concluída" if self.__status else "Não concluída"
        return super().__str__() + (
            f"\n Adversário: {self.__opponent}\n"
            f" Status: {status_text}"
        )