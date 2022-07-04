for msg in range(6, 0, - 1):
    print('Olá', msg)
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for n in range(i, f + 1, p):
    print(n)
s = 0
for u in range(0, 4):
    m = int(input('Digite um número: '))
    s += m
print('O somatório de todos os valores foi {}'.format(s))
print('Fim')
