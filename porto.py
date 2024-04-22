print('-'* 31)
print('    Centro Automotivo Porto')
print('-'* 31)

#criação de uma lista com os serviços disponiveis para o cliente
servicos = ['Alinhamento', 'Ar-condicionado', 'Arrefecimento', 
            'Balanceamento e geometria', 'Correias', 'Discos e Patilhas de Freio', 
            'Embreagens', 'Filtros e Velas de Ignição']

#criação de um dicionário para os orçamentos de cada serviço disponivel
orcamentos = {'alinhamento': 1300, 'Ar-condicionado': 300, 'Arrefecimento': 400, 
            'Balanceamento e geometria': 200, 'Correias': 300, 'Discos e Patilhas de Freio': 500,
            'Embreagens': 250, 'Filtros e Velas de Ignição': 375}

#lista criada para os veiculos que precisam serão adicionados
veiculos = []

while True:
    print(''' Menu de opções 
    [1] - Digite 1 para vizualizar o serviços disponiveis
    [2] - digite 2 para ver o orçamento de cada serviço
    [3] - digite 3 para cadastrar o veículo
    [4] - digite 4 para quantos veiculos estão cadastrados
    [5] - digite 5 para finalizar o programa''')
    

    escolha = int(input('digite sua escolha: '))

    if escolha == 1:
        for servico in servicos:
            print()
            print(f'- {servico}')
        print()   

    # Na escolha 2, o programa irá mostrar o serviço e seu orçamento (o para serviço e s para orçamento)
    elif escolha == 2:
        for s, o in orcamentos.items():
            print()
            print(f'- {s}: R${o}')
        print()

    # Na escolha 3, irá fazer um laço infinito para que o usuário possa cadastrar quantos veículos quiser, finalizará quando o usuarío digitar Nao
    elif escolha == 3:
        while True:
            print('-' * 25)
            nome_veiculo = input(' Nome do veiculo: ')
            print('-' * 25)
            veiculos.append(nome_veiculo)
            continuar = input('Deseja continuar? [Sim/Nao]').capitalize() # .capitalize() deixa a primeira letra maiuscula
            if continuar == 'Nao':
                break

    # Na escolha 4, a quantidade de veiculos cadastrados na lista veiculos será mostrada
    elif escolha == 4:
         print('-' * 30)
         print(f'Estão cadastrados {len(veiculos)} veiculo(s)')
         print('-' * 30)

    # Na escolha 5, o programa encerra
    elif escolha == 5:
        print('Finalizando o programa...')
        break
    
    # Ao digitar qualquer outra opção que não está no menu irá mostrar uma mensagem de opção invalida
    else:
        print('Opcao invalida! Digite novamente')
        print()
 