print("=== BEM-VINDO AO SEU ORGANIZADOR FINANCEIRO ===")
print("Criado por: Gabriel")
print("Versão: 1.0")
print()

# Vamos começar simples
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Vamos organizar suas finanças!")

transacoes = []

while True: 
    print("\nO que você gostaria de fazer?")
    print("1 - Adicionar um gasto")
    print("2 - Adicionar receita")
    print("3 - Ver todas as transações")
    print("4 - Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        print("Você escolheu adicionar um gasto. ")
        descricao = input("No que você gastou? ")
        valor = float(input("Quanto você gastou? "))
        transacoes.append({"tipo": "gasto", "descricao": descricao, "valor": valor})
        print(f"Você gastou R${valor} em {descricao}.")
        print("Gasto registrado!")
        
    elif opcao == '2':
        print("Você escolheu adicionar uma receita.")
        descricao = input("Qual a fonte da receita? ")
        valor = float(input("Quanto você recebeu? "))
        transacoes.append({"tipo": "receita", "descricao": descricao, "valor": valor})
        print(f"Você recebeu R${valor} de {descricao}")
        print("Receita registrada!")
        
    elif opcao == '3':
        print("\nAqui estão todas as suas transações:")
        
        if len(transacoes) == 0:
            print("Nenhuma transação registrada.")
        else:
            for i, transacao in enumerate(transacoes, 1):
                tipo = transacao["tipo"].upper()
                descricao = transacao["descricao"]
                valor = transacao["valor"]
                print(f"{i}. {tipo}: {descricao} - R${valor}")
        
    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente. ")
    