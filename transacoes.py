from datetime import datetime
from interface import obter_valor

def adicionar_gasto(transacoes):
    print("\nVocê escolheu adicionar um gasto. ")
    descricao = input("No que você gastou? ")
    valor = obter_valor("Quanto você gastou? ")
    
    print("Escolha uma categoria para o gasto:")
    print("1 - Alimentação")
    print("2 - Transporte")
    print("3 - Lazer")
    print("4 - Outros")
    opcao_cat = input("Digite o número da categoria: ")
    
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    categorias = {
        "1": "Alimentação",
        "2": "Transporte",
        "3": "Lazer",
        "4": "Outros"
    }
    categoria = categorias.get(opcao_cat, "Outros")
    
    transacoes.append({"tipo": "gasto", "descricao": descricao, "valor": valor, "categoria": categoria, "data": data_atual})
    print(f"Você gastou R${valor} em {descricao} ({categoria}).")
    print("Gasto registrado!")
    
def adicionar_receita(transacoes):
    print("\nVocê escolheu adicionar uma receita.")
    descricao = input("Qual a fonte da receita? ")
    valor = obter_valor("Quanto você recebeu? ")
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    transacoes.append({"tipo": "receita", "descricao": descricao, "valor": valor, "data": data_atual})
    print(f"Você recebeu R${valor} de {descricao}")
    print("Receita registrada!")
    
def mostrar_transacoes(transacoes):
    print("\nAqui estão todas as suas transações:")
        
    if len(transacoes) == 0:
        print("Nenhuma transação registrada.")
    else:
        for i, transacao in enumerate(transacoes, 1):
            tipo = transacao["tipo"].upper()
            descricao = transacao["descricao"]
            valor = transacao["valor"]
            data = transacao.get("data", "sem data")
            print(f"{i}. {tipo}: {descricao} - R${valor} ({data})")
                
        gastos = 0
        receitas = 0
            
        for transacao in transacoes:
            if transacao["tipo"] == "gasto":
                gastos += transacao["valor"]
            elif transacao["tipo"] == "receita":
                receitas += transacao["valor"]
        saldo = receitas - gastos
            
        print("\n--------ANÁLISE DOS DADOS--------")
        print(f"Total de gastos: R${gastos:.2f}")
        print(f"Total de receitas: R${receitas:.2f}")
        print(f"Saldo disponível: R${saldo:.2f}")
            
        total_gastos = 0
            
        for transacao in transacoes:
            if transacao["tipo"] == "gasto":
                total_gastos += 1
                    
        if gastos > 0:
            media_gastos = gastos / total_gastos
            print(f"A média dos seus gastos é de: R${media_gastos:.2f}")
    gastos_por_categoria = {}
    for transacao in transacoes:
        if transacao["tipo"] == "gasto":
            categoria = transacao.get("categoria", "Outros")
            gastos_por_categoria[categoria] = gastos_por_categoria.get(categoria, 0) + transacao["valor"]
            
    if gastos_por_categoria:
        print("\n--------GASTOS POR CATEGORIA--------")
        for categoria, total in gastos_por_categoria.items():
            print(f"{categoria}: R${total:.2f}")