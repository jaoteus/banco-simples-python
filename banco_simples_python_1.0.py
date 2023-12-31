'''
Meu perfil no Instagram @teuzonrails_
Meu perfil no GitHub: https://github.com/jaoteus
'''

'''
LEIA:
    Esta não é uma versão final, vocês poderão encontrar erros.
    Conforme eu vá adquirindo conhecimentos, irei estar sempre atualizando o código.
    Portanto, se encontrar algum erro, me avise, estarei agradecendo :)
'''
#Variáveis necessárias
saldo_cc = 0.0
saldo_cp = 0.0
valor = 0.0 #--> usado para fazer depósito e saque
nome_titular = 'João'
senha = 'jao0011' # --> por enquanto irá ficar fixa, apenas para teste.
cpf = '00000000011'
numero_conta_corrente = '1234-1' #--> por enquanto irá ficar fixa, apenas para teste.
numero_conta_poupanca = '1234-2' #--> por enquanto irá ficar fixa, apenas para teste.
agencia = '2332-9' #--> por enquanto irá ficar fixa, apenas para teste.
endereco = 'Rua Seilá, n°00, Recife, Pernambuco.' #--> por enquanto irá ficar fixa, apenas para teste.
numero = '+55 00 0000-0000' #--> por enquanto irá ficar fixa, apenas para teste.
opcao_menu = ''
email = 'jao0011@gmail.com' #--> por enquanto irá ficar fixa, apenas para teste.

#loops:
loop_login = True
loop_principal = True

# Função Menu principal
def menu_principal(): #--> o mesmo do Menu
    print('1 - Dados da conta')
    print('2 - Depósito na conta corrente')
    print('3 - Saque na conta corrente')
    print('4 - Déposito na conta poupança')
    print('5 - resgate na conta poupança')
    print('6 - Sair')

# Função para ver os dados da conta:
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

# Função para realizar um depósito na conta_corrente:
def deposito_cc():
    global valor, saldo_cc, loop_deposito, opcao_menu
    valor = float(input('Digite o valor desejado para depósito: R$'))
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

# Função para realizar um saque pela conta_corrente:
def saque_cc():
    global saldo_cc, valor
    valor = float(input('Digite o valor para o saque: R$'))
    if valor > saldo_cc:
        print('Saldo insuficiente!')
        valor = 0.0
    elif valor <= saldo_cc:
        saldo_cc = saldo_cc - valor
        valor = 0.0
    else:
        print('')

# Função para realizar um depósito na conta poupança (irá pegar da conta_corrente e transferir para a conta_poupança)
def deposito_cp():
    global valor, saldo_cp, saldo_cc
    valor = float(input('Digite o  valor para adicionar na conta poupança: R$'))
    if valor <= saldo_cc:
        saldo_cc = saldo_cc - valor
        saldo_cp = saldo_cp + valor
        print('Valor adicionado com sucesso!')
        valor = 0.0
    elif valor > saldo_cc:
        print('Saldo insuficiente na conta corrente!')
        valor = 0.0
    else:
        print('')

# Função para realizar um saque pela conta_poupança (irá pegar da conta_poupança e trasnferir de volta para a
# conta_corrente)
def saque_cp():
    global valor, saldo_cp, saldo_cc
    valor = float(input('Digite o valor para sacar na conta poupança: R$'))
    if valor > saldo_cp:
        print('Saldo insuficiente!')
        valor = 0.0
    elif valor <= saldo_cp:
        saldo_cp = saldo_cp - valor
        saldo_cc = saldo_cc + valor
        print('Saque realizado com sucesso!')
        valor = 0.0
    else:
        print('')

# 'Loop' para o usuario permanecer tentando fazer 'login' caso o mesmo não consiga e quando
# conseguir, o loop irá acabar e iremos direciona-lo para o menu.
while loop_login:
    # Entrada de dados do usuário
    email_ou_cpf = str(input('Digite seu e-mail ou CPF: '))
    senha_login = str(input('Digite sua senha: '))

    # Se todos forem corretos
    if (email_ou_cpf == email or email_ou_cpf == cpf) and senha_login == senha:
        print('Login efetuado com sucesso!')
        loop_login = False # Irá acabar com o laço de login, e irá ser direcionado para o loop do menu principal.

    # Se todos forem incorretos
    elif (email_ou_cpf != email or email_ou_cpf != cpf) and senha_login != senha:
        print('Login não efetuado, tente novamente!')
        continue # --> irá voltar para o inicio do loop para tentar logar novamente.

    #Se nenhum dos dois forem satisfeitos:
    else:
        print('Login não efetuado, tente novamente!')
        continue # --> irá voltar para o inicio do loop para tentar logar novamente.

# Menu principal
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
        loop_principal = False # --> Fim do programa
    else:
        print('Você digitou algo errado, tente novamente')
