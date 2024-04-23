print('-'* 31)
print('    Centro Automotivo Porto')
print('-'* 31)

#criação de uma lista com os serviços disponiveis para o cliente
servicos = ['Alinhamento', 'Ar-condicionado', 'Arrefecimento', 
            'Balanceamento e geometria', 'Correias', 'Discos e Patilhas de Freio', 
            'Embreagens', 'Filtros e Velas de Ignição']

#lista criada para os veiculos que precisam serão adicionados
veiculos = []

while True:
    print(''' Menu de opções 
    [1] - Digite 1 para vizualizar o serviços disponiveis
    [2] - digite 2 para cadastrar o veículo
    [3] - digite 3 para ver quantos veiculos estão cadastrados
    [4] - digite 4 para finalizar o programa''')
    

    escolha = int(input('digite sua escolha: '))

    if escolha == 1:
        for servico in servicos:
            print()
            print(f'- {servico}')
        print()   

     # Na escolha 2, irá fazer um laço infinito para que o usuário possa cadastrar os veículos que precisam de um diagnóstico, finalizará quando o usuarío digitar Nao
    elif escolha == 2:
        while True:
            print('-' * 25)
            nome_veiculo = input(' Nome do veiculo: ')
            print('-' * 25)
            veiculos.append(nome_veiculo)
            continuar = input('Deseja cadastrar outro? [Sim/Nao]').capitalize() # .capitalize() deixa a primeira letra maiuscula
            if continuar == 'Nao':
                break

    # Na escolha 3, a quantidade de veiculos cadastrados na lista veiculos será mostrada
    elif escolha == 3:
        print('-' * 30)
        print(f'Estão cadastrados {len(veiculos)} veiculo(s)')
        print('-' * 30)
    
     # Na escolha 4, o programa encerra
    elif escolha == 4:
        print('Finalizando o programa...')
        break

    # Ao digitar qualquer outra opção que não está no menu irá mostrar uma mensagem de opção invalida
    else:
        print('Opcao invalida! Digite novamente')
        print()
 