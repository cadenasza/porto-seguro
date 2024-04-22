print('-'* 31)
print('    Centro Automotivo Porto')
print('-'* 31)

servicos = ['Alinhamento', 'Ar-condicionado', 'Arrefecimento', 
            'Balanceamento e geometria', 'Correias', 'Discos e Patilhas de Freio', 
            'Embreagens', 'Filtros e Velas de Ignição']

orcamentos = {'alinhamento': 1300, 'Ar-condicionado': 300, 'Arrefecimento': 400, 
            'Balanceamento e geometria': 200, 'Correias': 300, 'Discos e Patilhas de Freio': 500,
            'Embreagens': 250, 'Filtros e Velas de Ignição': 375}

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

    elif escolha == 2:
        for o, p in orcamentos.items():
            print()
            print(f'- {o}: R${p}')
        print()

    elif escolha == 3:
        print('-' * 25)
        nome_veiculo = input(' Nome do veiculo: ')
        print('-' * 25)
        veiculos.append(nome_veiculo)

    elif escolha == 4:
         print('-' * 30)
         print(f'Estão cadastrados {len(veiculos)} veiculo(s)')
         print('-' * 30)

    elif escolha == 5:
        print('Finalizando o programa...')
        break
    
    else:
        print('Opcao invalida! Digite novamente')
        print()
 