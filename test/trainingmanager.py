import json
from event import Event
import datetime

class TrainingManager(Event):
    training_sessions = []
    loaded_ids = set()  

    def __init__(self, type, date, time, duration, location, professional):
        super().__init__(type, date, time, location)
        self.__duration = duration
        self.__professional = professional
        self.__status = False

        if self.get_id() not in TrainingManager.loaded_ids:
            TrainingManager.training_sessions.append(self)
            TrainingManager.loaded_ids.add(self.get_id())
            TrainingManager.save_to_json()
        else:
            print(f"Treino com ID {self.get_id()} já existe e não será adicionado novamente.")

    # Getters
    def get_duration(self):
        return self.__duration
    
    def get_professional(self):
        return self.__professional
    
    def get_status(self):
        return self.__status
    
    # Setters
    def set_duration(self, duration):
        self.__duration = duration
    
    def set_professional(self, professional):
        self.__professional = professional
    
    def set_status(self, status):
        self.__status = status
    
    def mark_completed(self):
        self.__status = True
        TrainingManager.save_to_json()
        return f"Treinamento de {self.get_type()} em {self.get_date()} foi concluído."

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.get_date()} {self.get_time()}", "%d/%m/%Y %H:%M")
            if datetime_evento < datetime.now():
                return "O treinamento já ocorreu."
            else:
                return "O treinamento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    @classmethod
    def save_to_json(cls, filename="trainings.json"):
        with open(filename, "w") as file:
            json.dump([training.to_dict() for training in cls.training_sessions], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="trainings.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.training_sessions = []  
                cls.loaded_ids = set()  
                for item in data:
                    if item["id"] not in cls.loaded_ids:  
                        training = TrainingManager(
                            item["type"],
                            item["date"],
                            item["time"],
                            item["duration"],
                            item["location"],
                            item["professional"]
                        )
                        training.__status = item["status"]
                        cls.training_sessions.append(training)
                        cls.loaded_ids.add(item["id"])
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        event_dict = super().to_dict()
        event_dict.update({
            "duration": self.__duration,
            "professional": self.__professional,
            "status": self.__status
        })
        return event_dict

    def __str__(self):
        status_text = "Concluído" if self.__status else "Agendado"
        return super().__str__() + (
            f"\nDuração: {self.__duration} min\n"
            f"Profissional: {self.__professional}\n"
            f"Status: {status_text}"
        )