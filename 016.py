from time import sleep
n1 = int(input('Digite um número: '))
sleep(1)
print('-=' * 15)
n2 = int(input('Digite outro número: '))
opçao = 0
while opçao != 5:
    print('-=' * 15)
    print(''' 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR
    ''')
    print('-=' * 15)
    opçao = int(input('Qual sua ação? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    sleep(2)
print('Fim do programa! volte sempre!')
