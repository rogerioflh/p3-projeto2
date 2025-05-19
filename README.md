1. Padrão Criacional: Factory Method

event.py
```
@classmethod
def create_event(cls, type, date, time, location):
    return cls(type, date, time, location)
```

finacial.py
```
@classmethod
def from_dict(cls, data):

@classmethod
def load_from_json(cls, filename="financial.json"):
```

player.py
```
@classmethod
def from_dict(cls, data):
    return cls(...)
```

recruitmentPlayer.py
```
@classmethod
def from_dict(cls, data):
    return cls(...)
```

user.py
```
@staticmethod
def criar_usuario_factory(tipo, nome, username, password):
    ...
```

2. Padrão Estrutural: Adapter, Decorator, Proxy

event.py -> Adpter
```
def to_json(self):
    return json.dumps(self.to_dict())
```

financial.py -> decorator
```
class FinancialDecorator:
    def __init__(self, financial):
        self._financial = financial

    def __getattr__(self, name):
        return getattr(self._financial, name)

    def print_summary(self):
        print(self._financial.__str__())
```

player.py -> decorator
```
class PlayerDecorator:
    def __init__(self, player):
        self._player = player

    def __getattr__(self, attr):
        return getattr(self._player, attr)

    def display_with_title(self):
        return f"*** Jogador Destaque ***\n{self._player}"
```

recruitmentPlayer.py -> Adpter
```
def to_json(self):
    return json.dumps(self.to_dict(), indent=4)
```

user.py -> Proxy
```
class UsuarioProxy:
    ...
```

3. Padrão Comportamental: Observer, Command-style update, Visitor

event.py -> Observer
```
# Atributo:
self._observers = []

# Métodos:
def add_observer(self, observer):
def remove_observer(self, observer):
def notify_observers(self, message):
```

financial.py -> Observer
```
self._observers = []

def register_observer(self, observer):
    ...
def remove_observer(self, observer):
    ...
def notify_observers(self, record):
    ...
```

```
def add_financial_record(...):
    ...
    self.notify_observers(record)
```

player.py -> Command-style update
```
def update(self, **kwargs):
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)
```

recruitmentPlayer.py -> Visitor
```
def accept(self, visitor):
    return visitor.visit(self)
```

```
class ProspectVisitor:
    def visit(self, prospect):
        return f"{prospect.name} ({prospect.position}), Age: {prospect.age}"
```

user.py -> Observer
```
def adicionar_observador(self, observador):
    self.observadores.append(observador)

def notificar_observadores(self, usuario):
    for obs in self.observadores:
        obs(usuario)
```

```
def novo_usuario_observador(usuario):
    print(f"Observador: Novo usuário criado -> {usuario}")
```

| Tipo de Padrão | Nome do Padrão | Onde está implementado                                |
| -------------- | -------------- | ----------------------------------------------------- |
| **Criacional**     | Factory Method | `create_event`                                        |
| **Estrutural**     | Adapter        | `to_json` (adapta para JSON)                          |
| **Comportamental** | Observer       | `add_observer`, `remove_observer`, `notify_observers` |
| **Criacional**     | Factory Method | `from_dict`, `load_from_json`                              |
| **Estrutural**     | Decorator      | `FinancialDecorator`                                       |
| **Comportamental** | Observer       | `register_observer`, `remove_observer`, `notify_observers` |
| **Criacional**     | Factory Method       | `from_dict`              |
| **Estrutural**     | Decorator            | `PlayerDecorator`        |
| **Comportamental** | Command-style Update | `update(self, **kwargs)` |
| **Criacional**     | Factory Method | `from_dict(cls, data)`                            |
| **Estrutural**     | Adapter        | `to_json(self)`                                   |
| **Comportamental** | Visitor        | `accept(self, visitor)` + `ProspectVisitor.visit` |
| **Criacional**     | Factory Method | `criar_usuario_factory()` no `GerenciadorUsuarios`                                          |
| **Estrutural**     | Proxy          | Classe `UsuarioProxy`                                                                       |
| **Comportamental** | Observer       | Métodos `adicionar_observador()` e `notificar_observadores()` + `novo_usuario_observador()` |
