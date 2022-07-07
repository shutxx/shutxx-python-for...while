s = c = 0
while True:
    n = int(input('Digite um número [digite 999 PARA PARAR]: '))
    if n == 999:
        break
    s += n
    c += 1
print('Fim')
print(f'Você digitou {c} e a soma foi {s}')
