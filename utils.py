# Função para garantir que o usuário digite um valor numérico válido
def obter_valor(mensagem):
    while True:
        entrada = input(mensagem).strip() # Recebe o valor do usuário e remove espaços em excesso
        entrada = entrada.replace(",", ".") # Permite que o usuário digite números com vírgula (ex: 25,50)
        try:
            valor = float(entrada) # Tenta converter a entrada em número float
            return valor
        except ValueError:
            # Se der erro, o usuário digitou algo inválido
            print("Valor inválido! Digite apenas números (ex: 25.50).")
            

# Função para garantir que o usuário digite um texto válido
def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        # Garante que o texto não esteja vazio
        if texto:
            return texto
        else:
            print("Digite algum texto!")
