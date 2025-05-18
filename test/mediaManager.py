import json
class MediaManager:
    _press_releases = []  # Atributo de classe encapsulado

    def __init__(self, title, content, date):
        self._title = title  # Atributo encapsulado
        self._content = content
        self._date = date
        MediaManager._press_releases.append(self)  # Adiciona à lista de releases

    # Getters e Setters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return (
            f" Título: {self._title}\n"
            f" Conteúdo: {self._content}\n"
            f" Data: {self._date}"
        )

    # Método para buscar um press release por título
    @classmethod
    def get_release_by_title(cls, title):
        for release in cls._press_releases:
            if release.title == title:
                return release
        return None

    # Método para remover um press release
    @classmethod
    def remove_release(cls, title):
        release = cls.get_release_by_title(title)
        if release:
            cls._press_releases.remove(release)
            print(f"Press Release '{title}' removido!")
        else:
            print(f"Press Release '{title}' não encontrado.")

    # Método para listar todos os press releases
    @classmethod
    def list_releases(cls):
        for release in cls._press_releases:
            print(release)
            
    @classmethod
    def save_to_json(cls, filename="press_releases.json"):
        with open(filename, "w") as file:
            json.dump([release.__dict__ for release in cls._press_releases], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="press_releases.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._press_releases = []
                for item in data:
                    release = MediaManager(item["_title"], item["_content"], item["_date"])
                    cls._press_releases.append(release)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")