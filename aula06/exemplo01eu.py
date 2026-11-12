compra = float(input('Informe o valor da compra: '))

print('''
[1] - Pix (12% de Desconto)
[2] - Debito (8% de desconto)
[3] - Crédito (5% de desconto)
[4] - Dinheiro (15% de desconto)
''')

desconto = 0
opcao = int(input('Qual a forma de pagamento? '))

match opcao:
    case 1:
        print('--- PIX ---')
        desconto = 0.12 * compra
        print(f'Seu desconto será de R$ {desconto}')
        print(f'O valor final da sua compra é de {compra - desconto}')
    case 2:
        print('--- DEBITO ---')
        desconto = 0.08 * compra
        print(f'Seu desconto será de R$ {desconto}')
        print(f'O valor final da sua compra é de {compra - desconto}')
    case 3:
        print('--- CREDITO ---')
        desconto = 0.05 * compra
        print(f'Seu desconto será de R$ {desconto}')
        print(f'O valor final da sua compra é de {compra - desconto}')
    case 4:
        print('--- DINHEIRO ---')
        desconto = 0.15 * compra
        print(f'Seu desconto será de R$ {desconto}')
        print(f'O valor final da sua compra é de {compra - desconto}')
    case _:
        print('--- OPÇÃO INVÁLIDA ---')