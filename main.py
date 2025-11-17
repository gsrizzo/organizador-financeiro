import json 
from interface import imprimir_cabecalho, obter_nome, mostrar_menu
from transacoes import adicionar_gasto, adicionar_receita, mostrar_transacoes

imprimir_cabecalho()    

# Pede o nome do usuário e dá uma mensagem de boas-vindas
nome = obter_nome()
print(f"Olá, {nome}! Vamos organizar suas finanças!")

transacoes = [] # Lista para armazenar as transações

# Tenta carregar transações salvas anteriormente
try:
    with open("transacoes.json", "r") as arquivo:
        transacoes = json.load(arquivo)
except FileNotFoundError:
    transacoes = [] # Caso o arquivo não exista, começa com uma lista vazia
            
# Loop principal do programa
while True: 
    opcao = mostrar_menu() # Mostra o menu e pega a opção do usuário
    
    # Adiciona um gasto
    if opcao == '1': 
        adicionar_gasto(transacoes)
        
    # Adiciona uma receita
    elif opcao == '2':
        adicionar_receita(transacoes)
        
    # Mostra todas as transações
    elif opcao == '3':
        mostrar_transacoes(transacoes)
                
    # Sai do programa salvando os dados
    elif opcao == '4':
        with open("transacoes.json", "w") as arquivo:
            json.dump(transacoes, arquivo, indent=4)
        print("Saindo do programa. Até mais!")
        break
    
    # Caso a opção seja inválida
    else:
        print("Opção inválida! Tente novamente. ")
    