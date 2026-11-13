for i in range(4):
    valor_final = float(input('Digite o valor da compra: '))
    if valor_final >= 200:
        desconto = valor_final * 0.9
        print(f'{desconto}')
    else:
        print(f'{valor_final}')
    