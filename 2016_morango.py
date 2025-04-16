retAL = int(input('Largura: '))
retAC = int(input('Comprimento: '))
retBL = int(input('Largura: '))
retBC = int(input('Comprimento: '))

a_ret_a = retAL*retAC
a_ret_b = retBL*retBC

if a_ret_a > a_ret_b:
    print(a_ret_a)
else:
    print(a_ret_b)