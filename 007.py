pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
déc = pri + (10 - 1) * raz
for cont in range(pri, déc + raz, raz):
    print('{} '.format(cont), end=', ')
print('Acabou')
