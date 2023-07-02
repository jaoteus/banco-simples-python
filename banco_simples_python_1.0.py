'''
Meu perfil no Instagram @teuzonrails_
Meu perfil no GitHub: https://github.com/jaoteus
'''

'''
LEIA:
    Esta não é uma versão final, vocês poderão encontrar erros.
    Conforme eu vá adquirindo conhecimentos, irei estar sempre atualizando o código.
    Portanto, se encontar algum erro, me avise, estarei agradecendo :)
'''
#Variáveis
saldo_cc = 0.0
saldo_cp = 0.0
valor = 0.0 #--> usado para fazer depósito e saque
nome_titular = 'Advogado José David Gil Rodrigues'
senha = 'alunoete123' # --> por enquanto irá ficar fixa, apenas para teste.
cpf = '000.000.000-11'
numero_conta_corrente = 1234-1 #--> por enquanto irá ficar fixa, apenas para teste.
numero_conta_poupanca = 1234-2 #--> por enquanto irá ficar fixa, apenas para teste.
agencia = 2332-9 #--> por enquanto irá ficar fixa, apenas para teste.
endereco = 'Rua Seilá, n°00, Recife, Pernambuco.' #--> por enquanto irá ficar fixa, apenas para teste.
numero = '+55 00 0000-0000' #--> por enquanto irá ficar fixa, apenas para teste.
opcao_menu = ''
email = 'alunoete123@gmail.com' #--> por enquanto irá ficar fixa, apenas para teste.

#loops:
loop_login = True
loop_principal = True

#Funções necessárias:
def menu_principal():
    print('1 - Dados da conta')
    print('2 - Depósito na conta corrente')
    print('3 - Saque na conta corrente')
    print('4 - Déposito na conta poupança')
    print('5 - resgate na conta poupança')
    print('6 - Sair')

def dados_da_conta():
    print(f'Seu nome: {nome_titular}')
    print(f'Seu e-mail: {email}')
    print(f'CPF: {cpf}')
    print(f'Seu núemro: {numero}')
    print(f'Seu endereço: {endereco}')
    print(f'Sua agência: {agencia}')
    print(f'Número da conta corrente: {numero_conta_corrente}')
    print(f'Número da conta poupança: {numero_conta_poupanca}')
    print(f'Seu saldo na conta corrente: R${saldo_cc:.2f}')
    print(f'Seu saldo na conta poupança: R${saldo_cp:.2f}\n')

def deposito_cc():
    global valor, saldo_cc, loop_deposito, opcao_menu
    valor = float(input('Digite o valor desejado para depósito: '))
    if valor >= 0.0:
        saldo_cc = saldo_cc + valor
        print('Valor depositado com sucesso!')
        valor = 0.0
        opcao_menu = ''
    elif valor < 0.0 or valor == 0.0:
        print('Digite um valor válido!')
        valor = 0.0
    else:
        print('')

def saque_cc():
    global saldo_cc, valor
    valor = float(input('Digite o valor para o saque: '))
    if valor > saldo_cc:
        print('Saldo insuficiente!')
        valor = 0.0
    elif valor <= saldo_cc:
        saldo_cc = saldo_cc - valor
        valor = 0.0
    else:
        print('')

def deposito_cp():
    global valor, saldo_cp, saldo_cc
    valor = float(input('Digite o  valor para adicionar na conta poupança: '))
    if valor <= saldo_cc:
        saldo_cc = saldo_cc - valor
        saldo_cp = saldo_cp + valor
        print('Valor adidionado com sucesso!')
        valor = 0.0
    elif valor > saldo_cc:
        print('Saldo insuficiente na conta corrente')
        valor = 0.0
    else:
        print('')

def saque_cp():
    global valor, saldo_cp, saldo_cc
    valor = float(input('Digite o valor para sacar na conta corrente: '))
    if valor > saldo_cp:
        print('Saldo insuficiente!')
        valor = 0.0
    elif valor <= saldo_cp:
        print('Saque realizado com sucesso!')
        valor = 0.0
    else:
        print('')

while loop_login:
    email_ou_cpf = str(input('Digite seu e-mail ou CPF: '))
    senha = str(input('Digite sua senha: '))

    if email_ou_cpf == 'alunoete123@gmail.com' or email_ou_cpf == '000.000.000-11' and senha == 'alunoete123':
        print('Login efetuado com sucesso!')
        loop_login = False

    elif email_ou_cpf != 'alunoete123@gmail.com' or email_ou_cpf != '000.000.000-11' and senha != 'alunoete123':
        print('Login não efetuado, tente novamente!')
        continue

    elif email_ou_cpf == 'alunoete123@gmail.com' or email_ou_cpf == '000.000.000-11' and senha != 'alunoete123':
        print('Login não efetuado, tente novamente!')
        continue

    else:
        print('')

while loop_principal:
    menu_principal()
    opcao_menu = input('Digite: ')
    if opcao_menu == '1':
        dados_da_conta()
    elif opcao_menu == '2':
        deposito_cc()
    elif opcao_menu == '3':
        saque_cc()
    elif opcao_menu == '4':
        deposito_cp()
    elif opcao_menu == '5':
        saque_cp()
    elif opcao_menu == '6':
        print('Saindo...')
        loop_principal = False
    else:
        print('Você digitou algo errado, tente novamente')
