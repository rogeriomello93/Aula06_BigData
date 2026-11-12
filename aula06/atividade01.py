valor_ingresso = float(input('Qual valor do ingresso? '))

print('''
[1] - Inteira
[2] - Meia entrada
[3] - Promoção
''')

tipo_ingresso = int(input('Selecione o tipo de ingresso:'))
desconto = 0

match tipo_ingresso:
    case 1:
        print('Inteira Selecionada')
    case 2:
        print('Meia Entrada selecionada')
        desconto = valor_ingresso * 0.5
    case 3:
        print('Promoção de 30% selecionada')
        desconto = valor_ingresso * 0.3
    case _:
        print('--- Opção Inválida ---')

if tipo_ingresso in [1, 2, 3]:
    valor_final = valor_ingresso - desconto
    print(f'Você deverá pagar R${valor_final:.2f} pelo ingresso')

else:
    print('--- Escolha uma das opções acima ---')