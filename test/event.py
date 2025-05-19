from abc import ABC, abstractmethod
import json
import uuid
from datetime import datetime

class Event(ABC):
    def __init__(self, type, date, time, location):
        self.__id = self.generate_id() 
        self.__type = type.capitalize()
        self.__date = date
        self.__time = time
        self.__location = location
        self._observers = []  # For observer pattern
    
    # Creational pattern: Factory method
    @classmethod
    def create_event(cls, type, date, time, location):
        return cls(type, date, time, location)
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4()) 
    
    # Observer pattern methods (Behavioral)
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(self, message)
    
    # Getters
    def get_id(self):
        return self.__id
    
    def get_type(self):
        return self.__type
    
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time
    
    def get_location(self):
        return self.__location
    
    # Setters
    def set_type(self, type):
        self.__type = type.capitalize()
    
    def set_date(self, date):
        self.__date = date
    
    def set_time(self, time):
        self.__time = time
    
    def set_location(self, location):
        self.__location = location
    
    def update_event_details(self, type=None, date=None, time=None, location=None):
        if type:
            self.set_type(type)
        if date:
            self.set_date(date)
        if time:
            self.set_time(time)
        if location:
            self.set_location(location)
        self.notify_observers("Event details updated")  # Notify observers on update

    @abstractmethod
    def check_status(self):
        #Método abstrato para verificar o status do evento.
        pass

    def to_dict(self):
        return {
            "id": self.__id,
            "type": self.__type,
            "date": self.__date,
            "time": self.__time,
            "location": self.__location
        }

    # Structural pattern: Adapter to JSON
    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return (
            f"ID: {self.__id}\n"
            f"Tipo: {self.__type}\n"
            f"Data: {self.__date}\n"
            f"Hora: {self.__time}\n"
            f"Localização: {self.__location}"
        )

# Example observer for demonstration
class EventObserver:
    def update(self, event, message):
        print(f"Observer notified for event {event.get_id()}: {message}")