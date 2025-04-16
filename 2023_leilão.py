n = int(input("lances: ")) #nº de lances recebidos 

if n > 0 and n <= 10000:

    nome_ganhador = ""
    lance_ganhador = 0

    for i in range(n):
        c= str(input("pessoa: "))
        v= int(input("lance: "))

        if len(c) > 1 and len(c) <= 10 and v > 0 and v <= 100000: 
            if v > lance_ganhador:
                nome_ganhador = c
                lance_ganhador = v

    print(nome_ganhador)
    print(lance_ganhador)

else:
    print("Programa encerrado! Obrigado por usar nosso programa!")








