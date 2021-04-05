Tests = int(input("Quantidade de testes: "))
i = 0
k = 0
x = ''
Char_Code = []

for i in range(Tests):
    str = input("Digite a string: ")
    Length = len(str)
    for k in range(Length):
        if k == 0:
            if str[k] != ' ':
                Char_Char = str[k]
                Char_Code.append(Char_Char)
        if str[k] == ' ':
            k = k + 1
            Char_Char = str[k]
            Char_Code.append(Char_Char)
    Decodificando = ''.join(x for x in Char_Code)
    print(Decodificando.lower())