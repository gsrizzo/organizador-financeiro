# Mostra um cabeçalho inicial para o usuário
def imprimir_cabecalho():
    print("=== BEM-VINDO AO SEU ORGANIZADOR FINANCEIRO ===")
    print("Criado por: Gabriel")
    print("Versão: 1.1")
    print()

# Pede o nome do usuário e garante que não fique vazio  
def obter_nome():
    nome = input("Qual é o seu nome? ").strip()
# Se o usuário não digitar nada, usa "Usuário" como padrão
    if nome == "":
        nome = "Usuário"
    return nome
    
# Mostra o menu principal e retorna a opção escolhida
def mostrar_menu():
        print("\n"+"="*40)
        print("MENU PRINCIPAL".center(40)) # Centraliza o texto
        print("="*40)
        print("1 - Adicionar gasto")
        print("2 - Adicionar receita")
        print("3 - Ver todas as transações")
        print("4 - Sair")
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ") # Recebe a escolha do usuário (não valida aqui, valida no main)
        return opcao
    

