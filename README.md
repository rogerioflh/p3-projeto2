## Para rodar o código, navegue até a pasta test e execute o código manager.py

## 1. Padrão Criacional: Factory Method

event.py
```
@classmethod
def create_event(cls, type, date, time, location):
    return cls(type, date, time, location)
```
Este método de classe é uma forma simples do Factory Method, pois encapsula a criação de instâncias da classe Event (ou de suas subclasses). Isso permite controlar ou estender a lógica de criação de objetos sem modificar diretamente o construtor.

---

finacial.py
```
@classmethod
def from_dict(cls, data):

@classmethod
def load_from_json(cls, filename="financial.json"):
```

Esses métodos são Factory Methods, pois criam instâncias da classe Financial com dados pré-configurados (por dicionário ou por JSON). Isso permite criar objetos de forma mais flexível e padronizada, encapsulando a lógica de criação.

---

player.py
```
@classmethod
def from_dict(cls, data):
    return cls(...)
```

Esse é o padrão Observer: a classe Financial permite registrar observadores que serão notificados (com update) sempre que um novo registro financeiro for adicionado. Isso promove o desacoplamento entre a lógica financeira e outras partes do sistema que reagem às mudanças.

---

recruitmentPlayer.py
```
@classmethod
def from_dict(cls, data):
    return cls(...)
```

Permite criar instâncias da classe RecruitmentManager a partir de um dicionário, encapsulando a lógica de construção. Esse é o padrão Factory Method.

---

user.py
```
@staticmethod
def criar_usuario_factory(tipo, nome, username, password):
    ...
```

Este método encapsula a lógica de criação de objetos do tipo Usuario e suas subclasses (Tecnico, Atleta, SecretarioFinanceiro, Gerente) com base em um identificador de tipo. Isso caracteriza o padrão Factory Method, pois fornece uma interface para criar objetos em subclasses.

---

## 2. Padrão Estrutural: Adapter, Decorator, Proxy

event.py -> Adpter
```
def to_json(self):
    return json.dumps(self.to_dict())
```
Esse método atua como um Adapter ao adaptar a estrutura de um objeto Event para o formato JSON. Ele encapsula a lógica de serialização para que o restante do sistema possa interagir com Event como se ele fosse diretamente compatível com JSON.

---

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

A classe FinancialDecorator é um Decorator que adiciona funcionalidade (no caso, print_summary) à classe Financial sem modificá-la diretamente. Ela intercepta chamadas com __getattr__, permitindo delegar qualquer método não definido ao objeto decorado.

---

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

A classe PlayerDecorator estende o comportamento da classe Player sem alterá-la diretamente. Ela utiliza __getattr__ para delegar os acessos ao objeto interno e adiciona o método display_with_title. Isso é um exemplo clássico do padrão Decorator.

---

recruitmentPlayer.py -> Adpter
```
def to_json(self):
    return json.dumps(self.to_dict(), indent=4)
```

O método to_json adapta um objeto da classe RecruitmentManager para o formato JSON. Isso representa um Adapter, pois adapta a interface do objeto para outro formato que pode ser consumido por sistemas externos (como arquivos ou APIs).

---

user.py -> Proxy
```
class UsuarioProxy:
    ...
```

UsuarioProxy atua como um substituto controlado para instâncias reais de Usuario, interceptando chamadas ao método autenticar. Esse é o padrão Proxy, pois adiciona uma camada intermediária para, por exemplo, logar acessos ou implementar controle de acesso sem alterar a classe real.

---

## 3. Padrão Comportamental: Observer, Command-style update, Visitor

event.py -> Observer
```
# Atributo:
self._observers = []

# Métodos:
def add_observer(self, observer):
def remove_observer(self, observer):
def notify_observers(self, message):
```

Esses métodos implementam o Observer Pattern. A classe Event mantém uma lista de "observadores" (objetos que implementam um método update) e os notifica quando há atualizações nos detalhes do evento (notify_observers é chamado, por exemplo, em update_event_details).

---

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

Esse é o padrão Observer: a classe Financial permite registrar observadores que serão notificados (com update) sempre que um novo registro financeiro for adicionado. Isso promove o desacoplamento entre a lógica financeira e outras partes do sistema que reagem às mudanças.

---

player.py -> Command-style update
```
def update(self, **kwargs):
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)
```

O método update encapsula a operação de atualizar atributos de um objeto com base em comandos dinâmicos (por chave-valor), o que se aproxima do padrão Command, mesmo que simplificado. Ele permite aplicar mudanças em tempo de execução de maneira desacoplada.

---

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

A classe RecruitmentManager permite que objetos externos (visitantes) operem sobre sua estrutura sem alterar sua definição. O método accept delega a lógica para o objeto visitor, conforme o padrão Visitor.

---

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

A classe GerenciadorUsuarios mantém uma lista de observadores e os notifica sempre que um novo usuário é criado. Isso caracteriza o padrão Observer, que permite que objetos interessados sejam automaticamente notificados quando ocorre uma mudança de estado

---

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
