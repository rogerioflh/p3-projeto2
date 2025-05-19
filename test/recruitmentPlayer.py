import json

class RecruitmentManager:
    _prospects_list = []

    def __init__(self, name, position, age, stats=None):
        self._name = name
        self._position = position
        self._age = age
        self._stats = stats if stats else {}
        RecruitmentManager._prospects_list.append(self)
        RecruitmentManager.save_to_json()

    # Creational Pattern: Factory Method
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            position=data.get("position"),
            age=data.get("age"),
            stats=data.get("stats", {})
        )

    # Structural Pattern: Adapter (to JSON string)
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    # Behavioral Pattern: Visitor
    def accept(self, visitor):
        return visitor.visit(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        RecruitmentManager.save_to_json()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        RecruitmentManager.save_to_json()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        RecruitmentManager.save_to_json()

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        self._stats = value
        RecruitmentManager.save_to_json()

    def evaluate_prospect(self, evaluation):
        self._stats["evaluation"] = evaluation
        RecruitmentManager.save_to_json()

    def to_dict(self):
        return {
            "name": self._name,
            "position": self._position,
            "age": self._age,
            "stats": self._stats
        }

    @classmethod
    def save_to_json(cls, filename="recruitment_data.json"):
        with open(filename, "w") as file:
            json.dump([prospect.to_dict() for prospect in cls._prospects_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="recruitment_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._prospects_list = []
                for item in data:
                    prospect = RecruitmentManager.from_dict(item)
                    cls._prospects_list.append(prospect)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    def __str__(self):
        return (
            f" Nome da possível contratação: {self._name}\n"
            f" Posição em que atua: {self._position}\n"
            f" Idade: {self._age}\n"
            f" Estatísticas: {self._stats}"
        )

    @classmethod
    def get_prospect_by_name(cls, name):
        for prospect in cls._prospects_list:
            if prospect.name == name:
                return prospect
        return None

# Example Visitor for the behavioral pattern
class ProspectVisitor:
    def visit(self, prospect):
        # Example: return a summary string
        return f"{prospect.name} ({prospect.position}), Age: {prospect.age}"