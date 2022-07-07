tot = totmil = menor = cont = 0
barato = ' '
while True:
    pro = str(input('Nome do produto: '))
    preco = float(input('preço R$: '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = pro
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R$:{tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$:1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
