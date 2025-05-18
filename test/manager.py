import json
import atexit
from datetime import datetime
from financial import Financial
from healthMonitor import HealthMonitor
from inventory import Inventory
from matchScheduler import MatchScheduler
from mediaManager import MediaManager
from player import Player
from performance import Performance
from recruitmentPlayer import RecruitmentManager
from trainingmanager import TrainingManager
from event import Event

# carregamento de dados do json
def load_data():
    Player.load_from_json()
    MatchScheduler.load_from_json()
    Financial.load_from_json()
    financeiro = Financial()
    Inventory.load_from_json()
    TrainingManager.load_from_json()
    
def menu_principal():
    while True:
        print("\n Bem vindo ao sistema de gerenciamento da sua equipe! Escolha como deseja proseguir: \n")
        print("1. Gerenciamento de Jogadores")
        print("2. Gerenciamento Financeiro")
        print("3. Gerenciamento de Compromissos")
        print("4. Gerenciamento de Equipamentos")
        print("5. Recrutamento de Jogadores")
        print("6. Gerenciamento de Mídia")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_jogadores()
            
        elif escolha == "2":
            menu_financeiro()
            
        elif escolha == "3":
            menu_eventos()
              
        elif escolha == "4":
            menu_equipamentos()
            
        elif escolha == "5":
            menu_recrutamento()
            
        elif escolha == "6":
            menu_midia()
            
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_jogadores():
    while True:
        print("\n Organização de atletas: \n")
        print("1. Adicionar Jogador")
        print("2. Ver informações sobre jogadores")
        print("3. Atualizar informações sobre um jogador")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do jogador: ")
            idade = int(input("Idade: "))
            altura = float(input("Altura (em metros): "))
            peso = float(input("Peso (em kg): "))
            posicao = input("Posição: ")
            passes = int(input("Passes: "))
            gols = int(input("Gols: "))
            assistencias = int(input("Assistências: "))
            defesas = int(input("Defesas: "))
            metros = int(input("Metros percorridos: "))
            lesao = input("Relatório de saúde: ")

            # Cria o jogador
            player = Player(nome, idade, altura, peso, posicao)

            # Cria o desempenho e o registro de saúde associados ao jogador
            performance = Performance(player, passes, gols, assistencias, defesas, metros)
            health = HealthMonitor(player, lesao)

            print("Jogador adicionado com sucesso!")

        elif escolha == "2":
            while True:
                print("Escolha qual ação deseja realizar:")
                print("1. Ver Jogadores da equipe")
                print("2. Ver status de saúde de um atleta")
                print("3. Ver desempenho de um atleta")
                print("0. Voltar ao menu principal")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    if not Player.players_list:
                        print("Nenhum jogador cadastrado.")
                    else:
                        for jogador in Player.players_list:
                            print(jogador)

                elif escolha == "2":
                    nome = input("Nome do jogador: ")
                    if nome in HealthMonitor.health_records:
                        print(f"Status de saúde de {nome}: {HealthMonitor.health_records[nome].injury_report}")
                    else:
                        print("Nenhum registro de saúde encontrado.")

                elif escolha == "3":
                    nome = input("Nome do jogador: ")
                    if nome in Performance.performance_data:
                        print(f"Desempenho de {nome}:")
                        print(f"Passes: {Performance.performance_data[nome].passes}")
                        print(f"Gols: {Performance.performance_data[nome].goals}")
                        print(f"Assistências: {Performance.performance_data[nome].assists}")
                        print(f"Defesas: {Performance.performance_data[nome].defenses}")
                        print(f"Metros percorridos: {Performance.performance_data[nome].meters}")
                    else:
                        print("Nenhum desempenho registrado.")

                elif escolha == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == "3":
            while True:
                print("Escolha qual ação deseja realizar:")
                print("1. Atualizar métricas de desempenho")
                print("2. Atualizar relatório de saúde de um atleta")
                print("0. Voltar ao menu principal")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome = input("Nome do jogador: ")
                    if nome in Performance.performance_data:
                        print("Selecione qual métrica deseja atualizar: ")
                        print("1. Passes")
                        print("2. Gols")
                        print("3. Assistências")
                        print("4. Defesas")
                        print("5. Metros percorridos")
                        escolha = input("Escolha uma opção: ")

                        if escolha == "1":
                            passes = int(input("Novo valor para passes: "))
                            Performance.performance_data[nome].update_info(passes=passes)
                        elif escolha == "2":
                            gols = int(input("Novo valor para gols: "))
                            Performance.performance_data[nome].update_info(goals=gols)
                        elif escolha == "3":
                            assistencias = int(input("Novo valor para assistências: "))
                            Performance.performance_data[nome].update_info(assists=assistencias)
                        elif escolha == "4":
                            defesas = int(input("Novo valor para defesas: "))
                            Performance.performance_data[nome].update_info(defenses=defesas)
                        elif escolha == "5":
                            metros = int(input("Novo valor para metros percorridos: "))
                            Performance.performance_data[nome].update_info(meters=metros)
                        else:
                            print("Opção inválida.")
                    else:
                        print("Jogador não encontrado.")

                elif escolha == "2":
                    nome = input("Nome do jogador: ")
                    if nome in HealthMonitor.health_records:
                        lesao = input("Novo relatório de lesão: ")
                        HealthMonitor.health_records[nome].update_info(lesao)
                        print("Relatório de saúde atualizado!")
                    else:
                        print("Jogador não encontrado.")

                elif escolha == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_financeiro():
    financeiro = Financial.load_from_json()  # Cria uma instância ao carregar os dados
    while True:
        print("\n Gerenciamento financeiro da equipe: o que deseja fazer?\n")
        print("1. Cadastrar Gasto ou Lucro")
        print("2. Ver Relatórios")
        print("3. Definir Metas Financeiras")
        print("4. Verificar Metas")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            record_type = input("Tipo (gasto/lucro): ")
            category = input("Categoria: ")
            amount = float(input("Valor: "))
            date = input("Data (dd/mm/aaaa): ")
            financeiro.add_financial_record(record_type, category, amount, date)
            print("Registro adicionado com sucesso!")

        elif escolha == "2":
            print("\n--- Relatórios ---")
            print("1. Mensal")
            print("2. Semestral")
            print("3. Anual")
            report_choice = input("Escolha uma opção: ")

            if report_choice == "1":
                month = int(input("Mês (1-12): "))
                year = int(input("Ano: "))
                summary = financeiro.get_monthly_summary(month, year)
                print(f"\nResumo Mensal ({month}/{year}):")
                print(f"Total de Gastos: R${summary['total_expenses']:.2f}")
                print(f"Total de Lucros: R${summary['total_revenue']:.2f}")
                print(f"Saldo: R${summary['balance']:.2f}")

            elif report_choice == "2":
                semester = int(input("Semestre (1 ou 2): "))
                year = int(input("Ano: "))
                summary = financeiro.get_semester_summary(semester, year)
                print(f"\nResumo Semestral (Semestre {semester}/{year}):")
                print(f"Total de Gastos: R${summary['total_expenses']:.2f}")
                print(f"Total de Lucros: R${summary['total_revenue']:.2f}")
                print(f"Saldo: R${summary['balance']:.2f}")

            elif report_choice == "3":
                year = int(input("Ano: "))
                summary = financeiro.get_annual_summary(year)
                print(f"\nResumo Anual ({year}):")
                print(f"Total de Gastos: R${summary['total_expenses']:.2f}")
                print(f"Total de Lucros: R${summary['total_revenue']:.2f}")
                print(f"Saldo: R${summary['balance']:.2f}")

        elif escolha == "3":
            goal_type = input("Tipo de meta (gasto/lucro): ")
            target_amount = float(input("Valor da meta: "))
            financeiro.set_financial_goal(goal_type, target_amount)
            print("Meta definida com sucesso!")

        elif escolha == "4":
            results = financeiro.check_goals()
            for goal_type, data in results.items():
                print(f"\nMeta de {goal_type.capitalize()}:")
                print(f"Meta: R${data['target']:.2f}")
                print(f"Realizado: R${data['actual']:.2f}")
                print(f"Atingida: {'Sim' if data['achieved'] else 'Não'}")

        elif escolha == "0":
            financeiro.save_to_json()  # Correto: chama o método na instância
            break
        else:
            print("Opção inválida. Tente novamente.")

def atualizar_detalhes_evento(evento):
    while True:
        print("\n  Atualizar detalhes de um compromisso")
        print("1. Tipo de Evento")
        print("2. Data do Evento")
        print("3. Hora do Evento")
        print("4. Localização do Evento")
        print("5. Voltar ao Menu Anterior")
        escolha = input("Escolha uma opção para atualizar ou voltar: ")

        if escolha == "1":
            novo_tipo = input("Digite o novo tipo de evento: ")
            evento.update_event_details(type=novo_tipo)
        elif escolha == "2":
            nova_data = input("Digite a nova data do evento (dd/mm/aaaa): ")
            evento.update_event_details(date=nova_data)
        elif escolha == "3":
            nova_hora = input("Digite a nova hora do evento (hh:mm): ")
            evento.update_event_details(time=nova_hora)
        elif escolha == "4":
            nova_localizacao = input("Digite a nova localização do evento: ")
            evento.update_event_details(location=nova_localizacao)
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

        print("Detalhes atualizados com sucesso:")
        print(evento)
        
def menu_treinamentos():
    while True:
        print("\n Administração de treinos.\n")
        print("1. Agendar treino")
        print("2. Ver treino")
        print("3. Marcar conclusão de treino")
        print("4. Verificar status de um treino")
        print("5. Atualizar detalhes de um treino")
        print("0. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo de treinamento: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")
            duracao = int(input("Duração (minutos): "))
            local = input("Local: ")
            profissional = input("Profissional responsável: ")
            TrainingManager(tipo, data, hora, duracao, local, profissional)
            print("Treino agendado!")
        elif escolha == "2":
            for treinamento in TrainingManager.training_sessions:
                print(treinamento)
        elif escolha == "3":
            id_evento = input("Digite o ID do treino que deseja concluir: ")
            for treinamento in TrainingManager.training_sessions:
                if treinamento.id == id_evento:
                    print(treinamento.mark_completed())
                    break
            else:
                print("Treino não encontrado")
        elif escolha == "4":
            id_evento = input("Digite o ID do treino que deseja consultar: ")
            found = False
            for treinamento in TrainingManager.training_sessions:
                if treinamento.get_id() == id_evento:  
                    print(treinamento.check_status())  
                    found = True
                    break
                if not found:
                    print("Treino não encontrado.")
        elif escolha == "5":
            id_evento = input("Digite o ID do treino que deseja atualizar: ")
            for treinamento in TrainingManager.training_sessions:
                if treinamento.id == id_evento:
                    atualizar_detalhes_evento(treinamento)
                    break
            else:
                print("Treino não encontrado.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_equipamentos():
    Inventory.load_from_json()  
    while True:
        print("\n  Gerenciamento de equipamentos do time\n")
        print("1. Adicionar um novo equipamento ao estoque")
        print("2. Ver equipamentos armazenados")
        print("3. Alterar disponibilidade de um equipamento")
        print("4. Editar informações de um equipamento")
        print("5. Remover um equipamento")
        print("6. Buscar equipamento por ID")
        print("7. Filtrar equipamentos por disponibilidade")
        print("0. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo do equipamento: ")
            setor = input("Setor: ")
            equipe = input("Equipe: ")
            ano = input("Ano de registro: ")
            ultimo_uso = input("Data do último uso (dd/mm/aaaa): ")
            Inventory(tipo, setor, equipe, ano, ultimo_uso)
            print("Equipamento adicionado!")

        elif escolha == "2":
            for equipamento in Inventory._inventory.values():
                print(equipamento)

        elif escolha == "3":
            id_equipamento = input("ID do equipamento: ")
            equipamento = Inventory.get_equipment_by_id(id_equipamento)
            if equipamento:
                equipamento.toggle_availability()
                print("Disponibilidade alterada!")
            else:
                print("Equipamento não encontrado.")

        elif escolha == "4":
            id_equipamento = input("ID do equipamento: ")
            equipamento = Inventory.get_equipment_by_id(id_equipamento)
            if equipamento:
                print("Deixe em branco para manter o valor atual.")
                tipo = input(f"Novo tipo ({equipamento.type_object}): ") or equipamento.type_object
                setor = input(f"Novo setor ({equipamento.sector}): ") or equipamento.sector
                equipe = input(f"Nova equipe ({equipamento.team}): ") or equipamento.team
                ano = input(f"Novo ano de registro ({equipamento.registration_year}): ") or equipamento.registration_year
                ultimo_uso = input(f"Nova data do último uso ({equipamento.last_use_date}): ") or equipamento.last_use_date
                equipamento.type_object = tipo
                equipamento.sector = setor
                equipamento.team = equipe
                equipamento.registration_year = ano
                equipamento.last_use_date = ultimo_uso
                print("Equipamento atualizado!")
            else:
                print("Equipamento não encontrado.")

        elif escolha == "5":
            id_equipamento = input("ID do equipamento: ")
            if id_equipamento in Inventory._inventory:
                del Inventory._inventory[id_equipamento]
                Inventory.save_to_json()
                print("Equipamento removido!")
            else:
                print("Equipamento não encontrado.")

        elif escolha == "6":
            id_equipamento = input("ID do equipamento: ")
            equipamento = Inventory.get_equipment_by_id(id_equipamento)
            if equipamento:
                print(equipamento)
            else:
                print("Equipamento não encontrado.")

        elif escolha == "7":
            disponibilidade = input("Filtrar por disponibilidade (1 - Disponível, 2 - Indisponível): ")
            if disponibilidade == "1":
                for equipamento in Inventory._inventory.values():
                    if equipamento.available:
                        print(equipamento)
            elif disponibilidade == "2":
                for equipamento in Inventory._inventory.values():
                    if not equipamento.available:
                        print(equipamento)
            else:
                print("Opção inválida.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_recrutamento():
    RecruitmentManager.load_from_json()  
    while True:
        print("\n Setor de análise de possíveis contratações")
        print("1. Adicionar novo atleta em monitoramento")
        print("2. Ver atletas em monitoramento")
        print("3. Avaliar atleta em monitoramento")
        print("4. Editar informações de um atleta")
        print("5. Remover um atleta")
        print("6. Buscar atleta por nome")
        print("7. Filtrar atletas por posição")
        print("8. Adicionar/Atualizar estatísticas de um atleta")
        print("0. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do atleta a ser monitorado: ")
            posicao = input("Posição: ")
            idade = int(input("Idade: "))
            RecruitmentManager(nome, posicao, idade)
            print("Atleta adicionado a lista de monitoramento!")

        elif escolha == "2":
            for prospecto in RecruitmentManager._prospects_list:
                print(prospecto)

        elif escolha == "3":
            nome = input("Nome do atleta: ")
            prospecto = RecruitmentManager.get_prospect_by_name(nome)
            if prospecto:
                avaliacao = input("Avaliação: ")
                prospecto.evaluate_prospect(avaliacao)
                print("Atleta avaliado!")
            else:
                print("Atleta não encontrado.")

        elif escolha == "4":
            nome = input("Nome do atleta: ")
            prospecto = RecruitmentManager.get_prospect_by_name(nome)
            if prospecto:
                print("Deixe em branco para manter o valor atual.")
                novo_nome = input(f"Novo nome ({prospecto.name}): ") or prospecto.name
                nova_posicao = input(f"Nova posição ({prospecto.position}): ") or prospecto.position
                nova_idade = input(f"Nova idade ({prospecto.age}): ") or prospecto.age
                prospecto.name = novo_nome
                prospecto.position = nova_posicao
                prospecto.age = nova_idade
                print("Informações do atleta atualizadas!")
            else:
                print("Atleta não encontrado.")

        elif escolha == "5":
            nome = input("Nome do atleta: ")
            prospecto = RecruitmentManager.get_prospect_by_name(nome)
            if prospecto:
                RecruitmentManager._prospects_list.remove(prospecto)
                RecruitmentManager.save_to_json()
                print("Atleta removido da lista de monitoramento!")
            else:
                print("Atleta não encontrado.")

        elif escolha == "6":
            nome = input("Nome do atleta: ")
            prospecto = RecruitmentManager.get_prospect_by_name(nome)
            if prospecto:
                print(prospecto)
            else:
                print("Atleta não encontrado.")

        elif escolha == "7":
            posicao = input("Posição para filtrar: ")
            for prospecto in RecruitmentManager._prospects_list:
                if prospecto.position == posicao:
                    print(prospecto)

        elif escolha == "8":
            nome = input("Nome do atleta: ")
            prospecto = RecruitmentManager.get_prospect_by_name(nome)
            if prospecto:
                chave = input("Nome da estatística (ex: gols, assistências): ")
                valor = input(f"Valor para {chave}: ")
                prospecto.stats[chave] = valor
                print(f"Estatística '{chave}' atualizada para '{valor}'!")
            else:
                print("Atleta não encontrado.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

import json

def menu_midia():
    MediaManager.load_from_json()  # Carrega os dados do JSON ao iniciar o menu
    while True:
        print("\n Gerenciamento de mídias da equipe!\n")
        print("1. Adicionar Press Release")
        print("2. Ver Press Releases")
        print("3. Editar Press Release")
        print("4. Remover Press Release")
        print("5. Buscar Press Release por Título")
        print("6. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            conteudo = input("Conteúdo: ")
            data = input("Data (dd/mm/aaaa): ")
            MediaManager(titulo, conteudo, data)
            MediaManager.save_to_json()
            print("Press Release adicionado!")

        elif escolha == "2":
            MediaManager.list_releases()

        elif escolha == "3":
            titulo = input("Título do Press Release a ser editado: ")
            release = MediaManager.get_release_by_title(titulo)
            if release:
                print("Deixe em branco para manter o valor atual.")
                novoTitulo = input(f"Novo título ({release.title}): ") or release.title
                novoConteudo = input(f"Novo conteúdo ({release.content}): ") or release.content
                novaData = input(f"Nova data ({release.date}): ") or release.date
                release.title = novoTitulo
                release.content = novoConteudo
                release.date = novaData
                MediaManager.save_to_json()
                print("Press Release atualizado!")
            else:
                print("Press Release não encontrado.")

        elif escolha == "4":
            titulo = input("Título do Press Release a ser removido: ")
            MediaManager.remove_release(titulo)
            MediaManager.save_to_json()

        elif escolha == "5":
            titulo = input("Título do Press Release: ")
            release = MediaManager.get_release_by_title(titulo)
            if release:
                print(release)
            else:
                print("Press Release não encontrado.")

        elif escolha == "6":
            MediaManager.save_to_json()
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_partidas():
    while True:
        print("\n Agendamento de partidas.\n")
        print("1. Agendar partida")
        print("2. Ver partidas agendadas")
        print("3. Verificar Status de uma partida")
        print("4. Marcar partida como concluída")
        print ("5. Atualizar informações de uma partida")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo da partida: ")
            local = input("Local: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")
            adversario = input("Adversário: ")
            MatchScheduler(tipo, local, data, hora, adversario)
            print("Partida agendada!")
        elif escolha == "2":
            for partida in MatchScheduler.competitions_list:
                print(partida)

            else:
                print("Partida não encontrada.")
                
                
        elif escolha == "3":
            id_evento = input("Digite o ID da partida que deseja consultar: ")
            for partida in MatchScheduler.competitions_list:
                if partida.get_id() == id_evento:  
                    print(partida.check_status())  
                    break
                else:
                    print("Partida não encontrada.")
                
        elif escolha == "4":
            id_evento = input("Digite o ID da partida que deseja concluir: ")
            for partida in MatchScheduler.competitions_list:
                if partida.id == id_evento:
                    print(partida.mark_as_completed())
                    break
            else:
                print("Partida não encontrada.")
                
        elif escolha == "5":
            id_evento = input("Digite o ID da partida que deseja atualizar: ")
            for partida in MatchScheduler.competitions_list:
                if partida.id == id_evento:
                    atualizar_detalhes_evento(partida)
                    break
            else:
                print("Treino não encontrado.")        
                
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_eventos():
    while True:
        print("\n Gerenciamento de compromissos da equipe\n")
        print("1. Gerenciamento de treinos")
        print("2. Agendamento de partidas")
        print("0. Voltar ao penu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_treinamentos()
        elif escolha == "2":
            menu_partidas()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")          
def load_data():
    try:
        Player.load_from_json()
        MatchScheduler.load_from_json()
        Financial.load_from_json()
        Inventory.load_from_json()
        TrainingManager.load_from_json()
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def save_data():
    try:
        Player.save_to_json()
        MatchScheduler.save_to_json()
       # Financial.save_to_json()
        Inventory.save_to_json()
        TrainingManager.save_to_json()
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

atexit.register(save_data)

if __name__ == "__main__":
    load_data()
    save_data()
    menu_principal()
    