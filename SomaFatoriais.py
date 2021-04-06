def SomaFatorial():
    Teste = int(input("Quantidade de testes: "))
    for i in range(Teste):
        n =  int(input("Numero: "))
        if n < 21 and n > 0:
            N_fat = 1
            Fat_Somado = []
            for i in range(2,n+1):
                N_fat = N_fat * i
            Fat_Somado.append(N_fat + N_fat)
            print(Fat_Somado)
SomaFatorial()
