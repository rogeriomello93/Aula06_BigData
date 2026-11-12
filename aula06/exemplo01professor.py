compra = float(input('Informe o valor da compra: '))

print('''
[1] - Pix (12% de Desconto)
[2] - Debito (8% de desconto)
[3] - Crédito (5% de desconto)
[4] - Dinheiro (15% de desconto)
''')

operacao = True
desconto = 0
opcao = int(input('Qual a forma de pagamento? '))

match opcao:
    case 1:
        print('--- PIX ---')
        desconto = 0.12 * compra
    case 2:
        print('--- DEBITO ---')
        desconto = 0.08 * compra
    case 3:
        print('--- CREDITO ---')
        desconto = 0.05 * compra
    case 4:
        print('--- DINHEIRO ---')
        desconto = 0.15 * compra  
    case _:
        operacao = False
        print('--- OPÇÃO INVÁLIDA ---')

if opcao in [1, 2, 3, 4]:
# if operacao == True:
# if desconto != 0: 
    valorfinal = compra - desconto
    print(f'Preço: {compra}')
    print(f'Seu desconto será de {desconto}')
    print(f'O valor final da sua compra é de {valorfinal}')

else:
    
    print('--- Escolha uma das opções acima ---')