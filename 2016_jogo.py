'''
Se p = 1 -> alice par
Se p = 0 -> alice impar
'''

p = int(input('0 para PAR e 1 para ÍMPAR: '))
d1 = int(input('dedos estendidos: '))
d2 = int(input('dedos estendidos: '))

if p == 0:
    if (d1+d2)%2 == 1:
        print('1')
    else: 
        print('0')
else:
    if (d1+d2)%2 == 0:
        print('1')
    else:
        print('0')

