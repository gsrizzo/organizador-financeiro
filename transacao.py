from datetime import datetime

# Classe que representa uma transação financeira
class Transacao:
    # Inicializa uma transação com tipo, descrição, valor, categoria e data
    def __init__(self, tipo, descricao, valor, categoria=None):
        self.tipo = tipo # Tipo da transação: "gasto" ou "receita"
        self.descricao = descricao # Texto explicando o que é a transação
        self.valor = valor # Valor numérico da transação
        self.categoria = categoria # Categoria do gasto (pode ser None para receitas)
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Data e hora da transação

    # Converte a transação em um dicionário para salvar em JSON
    def to_dict(self):
        return {
            "tipo": self.tipo,
            "descricao": self.descricao,
            "valor": self.valor,
            "categoria": self.categoria,
            "data": self.data
        }