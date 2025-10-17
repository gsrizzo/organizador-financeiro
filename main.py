def imprimir_cabecalho():
    print("=== BEM-VINDO AO SEU ORGANIZADOR FINANCEIRO ===")
    print("Criado por: Gabriel")
    print("Versão: 1.0")
    print()

def obter_nome():
    nome = input("Qual é o seu nome? ").strip()
    if nome == "":
        nome = "Usuário"
    return nome

def mostrar_menu():
        print("\n"+"="*40)
        print("           MENU PRINCIPAL")
        print("="*40)
        print("1 - Adicionar gasto")
        print("2 - Adicionar receita")
        print("3 - Ver todas as transações")
        print("4 - Sair")
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")
        return opcao
    
imprimir_cabecalho()    

nome = obter_nome()
print(f"Olá, {nome}! Vamos organizar suas finanças!")

transacoes = []

def adicionar_gasto(transacoes):
    print("\nVocê escolheu adicionar um gasto. ")
    descricao = input("No que você gastou? ")
    valor = float(input("Quanto você gastou? "))
    transacoes.append({"tipo": "gasto", "descricao": descricao, "valor": valor})
    print(f"Você gastou R${valor} em {descricao}.")
    print("Gasto registrado!")

def adicionar_receita(transacoes):
    print("\nVocê escolheu adicionar uma receita.")
    descricao = input("Qual a fonte da receita? ")
    valor = float(input("Quanto você recebeu? "))
    transacoes.append({"tipo": "receita", "descricao": descricao, "valor": valor})
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
            print(f"{i}. {tipo}: {descricao} - R${valor}")
                
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

while True: 
    opcao = mostrar_menu()
    if opcao == '1':
        adicionar_gasto(transacoes)
        
    elif opcao == '2':
        adicionar_receita(transacoes)
        
    elif opcao == '3':
        mostrar_transacoes(transacoes)
                
    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente. ")
    