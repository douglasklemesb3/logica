nome = input('digite seu nome completo: ')
idade = int(input('digite sua idade: '))
saldo = float(input('digite seu saldo: '))


print(
    '\ndigite (1) para saque'
    '\ndigite (2) para deposito'
    '\ndigite (3) para emprestimo'
    '\ndigite (4) para visualizar informaçoes'
    '\ndigite (qualquer outro caracter) para sair'
)
nada = input('')



def saques():
    saq = float(input('digite o valor do saque: '))
    if saq >= 1000 and saldo <= saq:
        print('saque nao aceito')
    else:
        print (saldo - saq)
        print('saque aprovado')

def deposito():
    dep = float(input('digite quanto quer depositar: '))
    if dep > 5000:
        print('deposito não autorizado')
    else:
        print(saldo + dep)
        print('seu deposito foi aprovado')

def visualizar():
    print(nome, idade,saldo)

def emprestimo():
    emp = float(input('digite quanto quer de deposito'))
    if idade <= 21:
        print('Idade invalida')
    elif saldo >= 1000 and emp >=2000 and saldo*15:
        print('saldo - emp')

if nada == '1':
    saques()
elif nada == '2':
    deposito()
elif nada == '4':
    visualizar()
