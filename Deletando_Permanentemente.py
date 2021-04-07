Varreduras = int(input("Enter the number of scans to be performed: "))
i = 0
k = 0
Conjunto_Bits_Deletados = []
try:
    for i in range(Varreduras):
        RastroBits = input("Enter the number os bits to be cleared: \n\n \t")
        Length = len(RastroBits)
        for k in range(Length):
            if k % 2 == 0:
                if RastroBits[k] == '0':
                    One = RastroBits[k].replace('0', '1')
                    Conjunto_Bits_Deletados.append(One)
                if RastroBits[k] == '1':
                    Zero = RastroBits[k].replace('1', '0')
                    Conjunto_Bits_Deletados.append(Zero)
            if k % 2 == 1:
                if RastroBits[k] == '1':
                    One = RastroBits[k].replace('1', '0')
                    Conjunto_Bits_Deletados.append(One)
                if RastroBits[k] == '0':
                    Zero = RastroBits[k].replace('0', '1')
                    Conjunto_Bits_Deletados.append(Zero)
        Deletion = ''.join(str(x) for x in Conjunto_Bits_Deletados)
        print(Deletion)
    print("Deletion succeeded")
except:
    print("Deletion failed")