class Usuario:
    def __init__(self, nome, username, password, role):
        self.nome = nome
        self.username = username
        self.password = password  
        self.role = role  

    def autenticar(self, username, password):
        return self.username == username and self.password == password

    def __str__(self):
        return f"Nome: {self.nome}, Username: {self.username}, Função: {self.role}"
    
class Tecnico(Usuario):
    def __init__(self, nome, username, password, especializacao):
        super().__init__(nome, username, password, role="técnico")
        self.especializacao = especializacao  

    def __str__(self):
        return super().__str__() + f", Especialização: {self.especializacao}"
    
class Atleta(Usuario):
    def __init__(self, nome, username, password, posicao):
        super().__init__(nome, username, password, role="atleta")
        self.posicao = posicao  

    def __str__(self):
        return super().__str__() + f", Posição: {self.posicao}"
    
class SecretarioFinanceiro(Usuario):
    def __init__(self, nome, username, password, setor):
        super().__init__(nome, username, password, role="secretário financeiro")
        self.setor = setor 

    def __str__(self):
        return super().__str__() + f", Setor: {self.setor}"
    
class Gerente(Usuario):
    def __init__(self, nome, username, password, departamento):
        super().__init__(nome, username, password, role="gerente")
        self.departamento = departamento 

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"
    
import json

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []
    def __init__(self):
        self.usuarios = []
        self.carregar_usuarios()

    def autenticar_usuario(self, username, password):
        """Autentica um usuário e retorna o objeto do usuário ou None se falhar."""
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return usuario  
        return None
    
    def criar_usuario(gerenciador):
        """Permite ao usuário criar um novo login no sistema"""
        print("\n Criar Novo Usuário")
        nome = input("Nome completo: ")
        username = input("Username: ")
        password = input("Senha: ")

        print("Escolha um tipo de usuário:")
        print("1 - Técnico")
        print("2 - Atleta")
        print("3 - Secretário Financeiro")
        print("4 - Gerente")

        tipo = input("Digite o número da opção: ")

        if tipo == "1":
            usuario = Tecnico(nome, username, password, "especialização indefinida")
        elif tipo == "2":
            usuario = Atleta(nome, username, password, "posição indefinida")
        elif tipo == "3":
            usuario = SecretarioFinanceiro(nome, username, password, "setor indefinido")
        elif tipo == "4":
            usuario = Gerente(nome, username, password, "departamento indefinido")
        else:
            print(" Tipo inválido!")
            return

        gerenciador.adicionar_usuario(usuario)
        print(" Usuário criado com sucesso! Agora você pode fazer login.")
    
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def salvar_usuarios(self, filename="usuarios.json"):
        with open(filename, "w") as file:
            json.dump([usuario.__dict__ for usuario in self.usuarios], file, indent=4)

    def carregar_usuarios(self, filename="usuarios.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.usuarios = []
                for item in data:
                    if item["role"] == "técnico":
                        self.usuarios.append(Tecnico(item["nome"], item["username"], item["password"], item["especializacao"]))
                    elif item["role"] == "atleta":
                        self.usuarios.append(Atleta(item["nome"], item["username"], item["password"], item["posicao"]))
                    elif item["role"] == "secretário financeiro":
                        self.usuarios.append(SecretarioFinanceiro(item["nome"], item["username"], item["password"], item["setor"]))
                    elif item["role"] == "gerente":
                        self.usuarios.append(Gerente(item["nome"], item["username"], item["password"], item["departamento"]))
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Iniciando com lista vazia.")