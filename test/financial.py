import json
from datetime import datetime
import os

class Financial:
    def __init__(self):
        self._annual_revenue = 0  
        self._monthly_revenue = 0  
        self._financial_records = []  
        self._monthly_expenses = {
            "folha_pagamento": 0,  
            "saude": 0,  
            "alimentacao": 0,  
            "manutencao": 0,  
            "viagens": 0,  
        }
        self._financial_goals = {} 

   
    @property
    def annual_revenue(self):
        return self._annual_revenue

    @annual_revenue.setter
    def annual_revenue(self, value):
        if value >= 0:
            self._annual_revenue = value
        else:
            raise ValueError("O faturamento anual não pode ser negativo.")

    @property
    def monthly_revenue(self):
        return self._monthly_revenue

    @monthly_revenue.setter
    def monthly_revenue(self, value):
        if value >= 0:
            self._monthly_revenue = value
        else:
            raise ValueError("O faturamento mensal não pode ser negativo.")

    @property
    def financial_records(self):
        return self._financial_records

    @property
    def monthly_expenses(self):
        return self._monthly_expenses

    @property
    def financial_goals(self):
        return self._financial_goals

    def add_financial_record(self, record_type, category, amount, date):
        """Adiciona um registro financeiro (gasto ou lucro)."""
        if record_type.lower() not in ["gasto", "lucro"]:
            raise ValueError("Tipo de registro inválido. Use 'gasto' ou 'lucro'.")
        
        record = {
            "type": record_type.lower(),
            "category": category,
            "amount": amount,
            "date": date,
        }
        self._financial_records.append(record)
        self.save_to_json()

    def get_monthly_summary(self, month, year):
        """Retorna um resumo financeiro mensal."""
        monthly_records = [
            record for record in self._financial_records
            if datetime.strptime(record["date"], "%d/%m/%Y").month == month
            and datetime.strptime(record["date"], "%d/%m/%Y").year == year
        ]
        total_expenses = sum(record["amount"] for record in monthly_records if record["type"] == "gasto")
        total_revenue = sum(record["amount"] for record in monthly_records if record["type"] == "lucro")
        return {
            "total_expenses": total_expenses,
            "total_revenue": total_revenue,
            "balance": total_revenue - total_expenses,
        }

    def get_semester_summary(self, semester, year):
        """Retorna um resumo financeiro semestral."""
        start_month = (semester - 1) * 6 + 1
        end_month = start_month + 5
        semester_records = [
            record for record in self._financial_records
            if start_month <= datetime.strptime(record["date"], "%d/%m/%Y").month <= end_month
            and datetime.strptime(record["date"], "%d/%m/%Y").year == year
        ]
        total_expenses = sum(record["amount"] for record in semester_records if record["type"] == "gasto")
        total_revenue = sum(record["amount"] for record in semester_records if record["type"] == "lucro")
        return {
            "total_expenses": total_expenses,
            "total_revenue": total_revenue,
            "balance": total_revenue - total_expenses,
        }

    def get_annual_summary(self, year):
        """Retorna um resumo financeiro anual."""
        annual_records = [
            record for record in self._financial_records
            if datetime.strptime(record["date"], "%d/%m/%Y").year == year
        ]
        total_expenses = sum(record["amount"] for record in annual_records if record["type"] == "gasto")
        total_revenue = sum(record["amount"] for record in annual_records if record["type"] == "lucro")
        return {
            "total_expenses": total_expenses,
            "total_revenue": total_revenue,
            "balance": total_revenue - total_expenses,
        }

    def set_financial_goal(self, goal_type, target_amount):
        """Define uma meta financeira."""
        if goal_type.lower() not in ["gasto", "lucro"]:
            raise ValueError("Tipo de meta inválido. Use 'gasto' ou 'lucro'.")
        self._financial_goals[goal_type.lower()] = target_amount
        self.save_to_json()

    def check_goals(self):
        """Verifica se as metas financeiras foram atingidas."""
        results = {}
        for goal_type, target_amount in self._financial_goals.items():
            if goal_type == "gasto":
                total = sum(record["amount"] for record in self._financial_records if record["type"] == "gasto")
            else:
                total = sum(record["amount"] for record in self._financial_records if record["type"] == "lucro")
            results[goal_type] = {
                "target": target_amount,
                "actual": total,
                "achieved": total >= target_amount if goal_type == "lucro" else total <= target_amount,
            }
        return results

    def save_to_json(self, filename="financial.json"):
        """Salva os dados financeiros em um arquivo JSON."""
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)
    @classmethod
    def load_from_json(cls, filename="financial.json"):
        """Carrega os dados financeiros de um arquivo JSON."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                finance = cls()  
                if isinstance(data, dict):  
                    finance._annual_revenue = data.get("annual_revenue", 0)
                    finance._monthly_revenue = data.get("monthly_revenue", 0)
                    finance._financial_records = data.get("financial_records", [])
                    finance._monthly_expenses = data.get("monthly_expenses", {})
                    finance._financial_goals = data.get("financial_goals", {})
                elif isinstance(data, list):  
                    for item in data:
                        finance._annual_revenue = item.get("annual_revenue", 0)
                        finance._monthly_revenue = item.get("monthly_revenue", 0)
                        finance._financial_records = item.get("financial_records", [])
                        finance._monthly_expenses = item.get("monthly_expenses", {})
                        finance._financial_goals = item.get("financial_goals", {})
                return finance
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
            return cls()  
        except json.JSONDecodeError:
            print(f"Erro: O arquivo {filename} contém JSON inválido. Iniciando com dados padrão.")
            return cls()  

    def to_dict(self):
        """Converte o objeto Financial em um dicionário."""
        return {
            "annual_revenue": self._annual_revenue,
            "monthly_revenue": self._monthly_revenue,
            "financial_records": self._financial_records,
            "monthly_expenses": self._monthly_expenses,
            "financial_goals": self._financial_goals,
        }

    def __str__(self):
        summary = self.get_financial_summary()
        return (
            f"Resumo Financeiro:\n"
            f"Faturamento Anual: R${self._annual_revenue:.2f}\n"
            f"Faturamento Mensal: R${self._monthly_revenue:.2f}\n"
            f"Gastos Mensais:\n"
            f"  - Folha de Pagamento: R${self._monthly_expenses['folha_pagamento']:.2f}\n"
            f"  - Saúde: R${self._monthly_expenses['saude']:.2f}\n"
            f"  - Alimentação: R${self._monthly_expenses['alimentacao']:.2f}\n"
            f"  - Manutenção: R${self._monthly_expenses['manutencao']:.2f}\n"
            f"  - Viagens: R${self._monthly_expenses['viagens']:.2f}\n"
        )