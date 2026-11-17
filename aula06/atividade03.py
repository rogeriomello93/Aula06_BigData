for i in range(5):
    valor_final = float(input('Digite o valor da compra: '))
    if valor_final >= 200:
        desconto = valor_final * .10
        final = valor_final - desconto
        print(f'O valor do desconto é de R${desconto:.2f}')
        print(f'O valor a ser pago é de R${final:.2f}')
    else:
        print(f'Você não teve desconto. O valor a ser pago é de R$ {valor_final}')
    