import json 
from interface import imprimir_cabecalho, obter_nome, mostrar_menu, obter_valor
from transacoes import adicionar_gasto, adicionar_receita, mostrar_transacoes

imprimir_cabecalho()    

nome = obter_nome()
print(f"Olá, {nome}! Vamos organizar suas finanças!")

transacoes = []

try:
    with open("transacoes.json", "r") as arquivo:
        transacoes = json.load(arquivo)
except FileNotFoundError:
    transacoes = []
            

while True: 
    opcao = mostrar_menu()
    if opcao == '1':
        adicionar_gasto(transacoes)
        
    elif opcao == '2':
        adicionar_receita(transacoes)
        
    elif opcao == '3':
        mostrar_transacoes(transacoes)
                
    elif opcao == '4':
        with open("transacoes.json", "w") as arquivo:
            json.dump(transacoes, arquivo, indent=4)
        print("Saindo do programa. Até mais!")
        break
    
    else:
        print("Opção inválida! Tente novamente. ")
    