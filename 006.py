soma = 0
conti = 0
for cont in range(1, 7):
    num = int(input('Digite o {}º número: '.format(cont)))
    if num % 2 == 0:
        soma += num
        conti += 1
print('Você informou {} números pares e a soma foi {}'.format(conti, soma))
