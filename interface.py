def imprimir_cabecalho():
    print("=== BEM-VINDO AO SEU ORGANIZADOR FINANCEIRO ===")
    print("Criado por: Gabriel")
    print("Versão: 1.1")
    print()
    
def obter_nome():
    nome = input("Qual é o seu nome? ").strip()
    if nome == "":
        nome = "Usuário"
    return nome
    
def mostrar_menu():
        print("\n"+"="*40)
        print("MENU PRINCIPAL".center(40))
        print("="*40)
        print("1 - Adicionar gasto")
        print("2 - Adicionar receita")
        print("3 - Ver todas as transações")
        print("4 - Sair")
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")
        return opcao
    
def obter_valor(mensagem):
    while True:
        entrada = input(mensagem).strip()
        entrada = entrada.replace(",", ".")  
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Valor inválido! Digite apenas números (ex: 25.50).")
