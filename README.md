# Organizador-financeiro
Sistema de controle financeiro pessoal desenvolvido em Python.

**Criado por:** Gabriel  
**Versão:** 1.3 (Atualizado em 2026-01-13)

##  Sobre o projeto

Este projeto tem como objetivo ajudar o usuário a registrar e acompanhar suas finanças pessoais de forma simples. 

O sistema permite cadastrar gastos e receitas, visualizar transações e gerar análises básicas automaticamente.

Os dados são armazenados localmente em um arquivo JSON, garantindo persistência entre execuções do programa.

Projeto desenvolvido para consolidar conhecimentos em Python e desenvolvimento.

## Destaques técnicos  
- Persistência de dados com JSON  
- Menu interativo no terminal  
- Estrutura baseada em funções  
- Cálculo automático de métricas financeiras

### Funcionalidades:

🔹 Registro de transações

- Adicionar gastos
- Adicionar receitas
- Registro automático de data e hora
- Classificação de gastos por categoria

🔹 Visualização

- Listagem de todas as transações registradas
- Exibição de tipo, descrição, valor, categoria e data

🔹 Análises financeiras automáticas

- Total de gastos
- Total de receitas
- Saldo atualizado com cores no terminal:
    - Verde = saldo positivo
    - Vermelho = saldo negativo
    - Amarelo = saldo neutro
- Média dos gastos
- Total de gastos por categoria

🔹 Outros recursos

- Menu interativo no terminal
- Loop contínuo de execução (o programa não fecha sozinho)
- Salvamento automático em arquivo 'transacoes.json'

### Como usar:

1. Clone o repositório:
    git clone https://github.com/gsrizzo/organizador-financeiro.git
2. Acesse a pasta do projeto:
    cd organizador-financeiro
3. Execute o programa: `python main.py`
4. Digite seu nome
5. Utilize o menu para registrar e visualizar suas finanças

##  Próximas funcionalidades planejadas:
- [ ] Análises mais avançadas utilizando pandas
- [ ] Gráficos interativos
- [ ] Exportar relatórios em CSV 
- [ ] Interface web simples

##  Tecnologias:
- Python 3
- Lógica de programação
- Análise básica de dados
- Programação orientada a objetos
- Git/GitHub
- JSON (para salvar os dados)

---
*Projeto desenvolvido durante aprendizado de programação e Ciência de Dados*

Autor: Gabriel Rizzo  
Em constante evolução 🚀
