print("=== BEM-VINDO AO SEU ORGANIZADOR FINANCEIRO ===")
print("Criado por: Gabriel")
print("Versão: 1.0")
print()

# Vamos começar simples
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Vamos organizar suas finanças!")

while True: 
    print("\nO que você gostaria de fazer?")
    print("1 - Adicionar um gasto")
    print("2 - Adicionar receita")
    print("3 - Sair")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        print("Você escolheu adicionar um gasto. ")
        descricao = input("No que você gastou? ")
        valor = float(input("Quanto você gastou? "))
        print(f"Você gastou R${valor} em {descricao}.")
        print("Gasto registrado!")
        
    elif opcao == '2':
        print("Você escolheu adicionar uma receita.")
        descricao = input("Qual a fonte da receita? ")
        valor = float(input("Quanto você recebeu? "))
        print(f"Você recebeu R${valor} de {descricao}")
        print("Receita registrada!")
        
    elif opcao == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente. ")
    