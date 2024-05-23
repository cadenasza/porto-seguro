#criação de uma lista com os serviços disponiveis para o cliente
servicos = ['Alinhamento', 'Ar-condicionado', 'Arrefecimento', 
            'Balanceamento e geometria', 'Correias', 'Discos e Patilhas de Freio', 
            'Embreagens', 'Filtros e Velas de Ignição']

#lista criada para os veiculos que serão adicionados
veiculos = []

#lista criada para os placa dos veiculos que serão adicionados
placas = []

#Dicionario do para o cadastro do cliente
clientes = {}

# função criada para o menu do programa
def menu():
    print('-'* 40)
    print('    Centro Automotivo Porto\n')
    print(''' Menu de opções 
    [1] - Digite 1 para vizualizar o serviços disponiveis
    [2] - digite 2 para cadastrar o veículo
    [3] - digite 3 para ver quais veiculos estão cadastrados
    [4] - digite 4 para se cadastrar
    [5] - digite 5 para finalizar o programa''')
    print('-'* 40)


# função criada para mostrar os servicos disponiveis
def servicos_disponiveis(servicos):
    for servico in servicos:
        print()
        print(f'- {servico}')
             


#função criada para o cadastro de veiculos, nas listas veiculos e placas
def cadastro_veiculo():
    while True:
        print('-' * 25)
        nome_veiculo = input(' Nome do veiculo: ')
        placa_veiculo = input('Placa do veiculo: ')
        veiculos.append(nome_veiculo)
        placas.append(placa_veiculo)
        print('-' * 25)
        continuar = input('Deseja cadastrar outro? [Sim/Nao]').capitalize() # .capitalize() deixa a primeira letra maiuscula
        if continuar == 'Nao':
            break


#função criada para ver o nome de cada carro cadastrado
def veiculos_cadastrados(veiculos, placas):
    print('-' * 30)
    for pos, veiculo in enumerate(veiculos):
        print(f'{pos + 1}- Veiculo: {veiculo}')
    for posicao, placa in enumerate(placas):
        print(f'{posicao + 1}- Placa: {placa}')  

# Função criada para o cadastro do cliente com nome e email
def cadastro_cliente(clientes):
    print('Cadastro')
    print('-'*30)
    clientes['nome'] = input('Nome: ')
    clientes['email'] = input('Email: ')
    print('Cadastro realizado!')
    print('-'*30)
    

# funcao principal do programa            
def main():
    while True:
        menu()
        escolha = int(input('digite sua escolha: '))

        # Na escolha 1, a função serviços_disponiveis é chamada
        if escolha == 1:
            print(servicos_disponiveis(servicos))

        # Na escolha 2, a função cadastro_veiculo é chamada
        elif escolha == 2:
            cadastro_veiculo()

        # Na escolha 3, a função veiculos_cadastrados é chamada
        elif escolha == 3:
            veiculos_cadastrados(veiculos, placas)

        elif escolha == 4:
            cadastro_cliente(clientes)

        # Na escolha 4, o programa encerra
        elif escolha == 5:
            print('Finalizando o programa...')
            break

        # Ao digitar qualquer outra opção que não está no menu irá mostrar uma mensagem de opção invalida
        else:
            print('Opcao invalida! Digite novamente')
            print()
                    
# função main chamada 
main()
