"""

    **********************************************************************************************
    *                                                                                            *   
    *   Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra      *
    *   subsequente for o oposto da letra anterior. Espaços devem ser ignorados ao determinar    *
    *   o case (minúsculo/maiúsculo) de uma letra. Por exemplo, "A b Cd" é uma sentença          *
    *   dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula,   *
    *   a próxima letra ('C') é maiúscula, e a próxima letra ('d') é minúscula.                  *
    *                                                                                            *
    **********************************************************************************************


"""

def SentencaDancanteUpper():
    k = 0
    Testes = int(input("Quantidade de testes: "))
    for k in range(Testes):
        StringDancante = input("Digite a sentença: ")
        Range = len(StringDancante)
        i = 0
        Dance = []
        for i in range(Range):
            if i % 2 == 0:
                par = StringDancante[i].upper()
                Dance.append(par)
            if i % 2 != 0:
                impar = StringDancante[i].lower()
                Dance.append(impar)
        Dancando = ''.join(str(x) for x in Dance)
        print(Dancando)

SentencaDancanteUpper()