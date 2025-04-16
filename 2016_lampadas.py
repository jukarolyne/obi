'''
A -> lampada A
B -> lampada B
I1 -> interruptor 1 (ao apertar, A troca de estado)
I2  -> interruptor 2 (ao apertar, as duas lampadas trocam de estado)
0 -> apagado
1 -> aceso
'''

a = 0
b = 0
acoes = []

n = int(input('números de vezes que aperta interruptor: '))

for i in range(n):
    acao = int(input('1 para interruptor 1 e 2 para interruptor 2: '))
    acoes.append(acao)

for i in acoes:
    if i == 1:
        if a == 0:
            a = 1
        else:
            a = 0
    else:
        if a == 0 and b == 0:
            a = 1
            b = 1
        elif a == 0 and b == 1:
            a = 1
            b = 0
        elif a == 1 and b == 0:
            a = 0
            b = 1
        else:
            a = 0
            b = 0
    
print(a)
print(b)