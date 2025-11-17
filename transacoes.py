from utils import obter_valor
from transacao import Transacao

# Registra um novo gasto na lista de transações
def adicionar_gasto(transacoes):
    print("\nVocê escolheu adicionar um gasto. ")
    descricao = input("No que você gastou? ") # Descrição do gasto escrita pelo usuário
    valor = obter_valor("Quanto você gastou? ") # Valor já validado (somente números)
    
    # Menu de categorias para organizar melhor os gastos
    print("Escolha uma categoria para o gasto:")
    print("1 - Alimentação")
    print("2 - Transporte")
    print("3 - Lazer")
    print("4 - Outros")
    opcao_cat = input("Digite o número da categoria: ") # Usuário escolhe a categoria pelo número
    
    # Dicionário que converte número em texto da categoria
    categorias = {
        "1": "Alimentação",
        "2": "Transporte",
        "3": "Lazer",
        "4": "Outros"
    }
    categoria = categorias.get(opcao_cat, "Outros") # Usa a categoria escolhida ou "Outros" como padrão
    
    transacao = Transacao("gasto", descricao, valor, categoria) # Cria uma transação do tipo gasto
    transacoes.append(transacao.to_dict()) # Adiciona a transação na lista como dicionário
    print(f"Você gastou R${valor} em {descricao} ({categoria}).")
    print("Gasto registrado!")
    
# Registra uma nova receita na lista de transaçõe
def adicionar_receita(transacoes):
    print("\nVocê escolheu adicionar uma receita.")
    descricao = input("Qual a fonte da receita? ") # Texto simples com a descrição da receita
    valor = obter_valor("Quanto você recebeu? ") # Valor da receita validado
    transacao = Transacao("receita", descricao, valor) # Cria uma transação do tipo receita
    transacoes.append(transacao.to_dict()) # Adiciona a transação na lista como dicionário
    print(f"Você recebeu R${valor} de {descricao}")
    print("Receita registrada!")
    
# Lista todas as transações, soma gastos, receitas e mostra relatórios
def mostrar_transacoes(transacoes):
    print("\nAqui estão todas as suas transações:")
    
    # Se não houver nada registrado, avisa o usuário    
    if len(transacoes) == 0:
        print("Nenhuma transação registrada.")
    else:
        # Mostra todas as transações registradas
        for i, transacao in enumerate(transacoes, 1):
            tipo = transacao["tipo"].upper()
            descricao = transacao["descricao"]
            valor = transacao["valor"]
            data = transacao.get("data", "sem data") # Caso não tenha data salva
            print(f"{i}. {tipo}: {descricao} - R${valor} ({data})")
                
        gastos = 0
        receitas = 0
        
        # Soma separando gastos e receitas    
        for transacao in transacoes:
            if transacao["tipo"] == "gasto":
                gastos += transacao["valor"]
            elif transacao["tipo"] == "receita":
                receitas += transacao["valor"]
        saldo = receitas - gastos
        
        # Relatório geral    
        print("\n--------ANÁLISE DOS DADOS--------")
        print(f"Total de gastos: R${gastos:.2f}")
        print(f"Total de receitas: R${receitas:.2f}")
        print(f"Saldo disponível: R${saldo:.2f}")
        
        # Cálculo da média de gastos    
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