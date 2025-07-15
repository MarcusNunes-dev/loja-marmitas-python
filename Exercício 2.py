#Menu de boas vindas da loja de marmitas
print('-' * 6, 'Boas vindas à loja do Marcus Vinicius da Silva Nunes!', '-' * 6)
print('-' * 26, 'Cardápio', '-' * 31)
print('-' * 67)
print('---', '|', ' Tamanho ', '|', ' Bife Acebolado (BA) ', '|', 'Filé de Frango(FF) ', '|', '---')
print('---', '|', '   P     ', '|', '      R$ 16.00       ', '|', '      R$ 15.00     ', '|', '---')
print('---', '|', '   M     ', '|', '      R$ 18.00       ', '|', '      R$ 17.00     ', '|', '---')
print('---', '|', '   G     ', '|', '      R$ 22.00       ', '|', '      R$ 21.00     ', '|', '---')

totalPedido = 0.0 #Variável declarada para o valor total do pedido


while True: #loop principal do código
    while True: #loop da escolha do sabor
        sabor = input('\nEscolha o sabor desejado (BA/FF): ').upper()
        porExtenso = ''
        if sabor == 'BA':
            porExtenso = 'Bife Acebolado'
        elif sabor == 'FF':
            porExtenso = 'File de Frango'

        if sabor == 'BA' or sabor == 'FF':
            print(f'Você escolheu {porExtenso}!')
            break
        else:
            print('Sabor inválido! Tente novamente.')
            continue

    while True: #loop da escolha do tamanho
        tamanho = input('\nEscolha o tamanho (P/M/G): ').upper()
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            print(f'Você pediu {porExtenso} no tamanho {tamanho}!')
            break
        else:
            print('Tamanho inválido! Tente novamente.')
            continue

    preco_item = 0.0 #varíavel declarada para o preço do item

#Definição dos preços de cada item e tamanho
    if sabor == 'BA':
        if tamanho == 'P':
            preco_item = 16.00
        elif tamanho == 'M':
            preco_item = 18.00
        elif tamanho == 'G':
            preco_item = 22.00

    elif sabor == 'FF':
        if tamanho == 'P':
            preco_item = 15.00
        elif tamanho == 'M':
            preco_item = 17.00
        elif tamanho == 'G':
            preco_item = 21.00

#acumulador dos itens e tamanho selecionados para resultado final em "totalPedido
    totalPedido += preco_item

#Saída de console informando o sabor e o tamanho escolhido, resultando ao final no preço de acordo com o sabor e tamanho escolhidos
    print(f'Você escolheu {porExtenso} no tamanho {tamanho}: R$ {preco_item:.2f}')

#loop para a escolha de mais algum pedido
    while True:
        pedirmais = input('\nDeseja pedir mais alguma coisa? (SIM/NAO): ').upper()
        #Se a escolha for SIM, voltamos ao ínicio com a escolha do sabor e do tamanho
        if pedirmais == 'SIM':
            break
        #Se a escolha for NAO, saída de console com o valor total do pedido dos itens selecionados
        elif pedirmais == 'NAO':
            print(f'\nO valor total do seu pedido é: R${totalPedido:.2f}')
            break
        #Se não for digitado SIM ou NAO, respostá inválida, pedindo para digitar apenas SIM ou NAO
        else:
            print('Resposta inválida! Por favor, digite apenas SIM ou NAO')
            continue

#Finalização do programa, caso não queria pedir mais nada.
    if pedirmais == 'NAO':
        break






