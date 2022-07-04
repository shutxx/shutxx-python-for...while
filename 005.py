from time import sleep
cont = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    # res = cont * c
    sleep(1)
    print('{} x {:2} = {}'.format(cont, c, cont*c))
