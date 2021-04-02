"""
    *******************************************************************************************************
    *    Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las,        *   
    *    alternando as letras de cada string, começando com a primeira letra da primeira string, seguido  * 
    *    pela primeira letra da segunda string, em seguida pela segunda letra da primeira string, e assim * 
    *    sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string  *
    *    resultante e retornada.                                                                          *  
    *                                                                                                     *  
    *    Entrada                                                                                          *  
    *    A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a        *  
    *    quantidade    *    de casos de teste que vem a seguir. Cada caso de teste é composto por         *  
    *    uma linha que contém duas cadeias de caracteres,    *    cada cadeia de caracteres contém        *
    *     entre 1 e 50 caracteres inclusive.                                                              *  
    *                                                                                                     *  
    *    Saída                                                                                            *  
    *    Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a       *
    *    cadeia resultante.                                                                               *  
    *                                                                                                     *
    *                                                                                                     *      
    *                                                                                                     *  
    *    Exemplo de Entrada  	Exemplo de Saída                                                          *  
    *        2                                                                                            *      
    *        tpo ocder              topcoder                                                              *          
    *        aa bb                  abab                                                                  *              
    *                                                                                                     *  
    *******************************************************************************************************
"""
def __Combinador__():
    Qtd_String  = int(input("Quantidade de casos de teste: "))
    i = 0
    k = 0
    j = 0
    for i in range(Qtd_String):
        string1  = input()
        Length1  = len(string1)
        string2  = input()
        Length2  = len(string2)
        a = []
        for k in range(Length2):
            if k % 2 == 0:
                S1 = string1[k]
                a.append(S1.lower())
                S2 = string2[k]
                a.append(S2.lower())
            if k % 2 != 0:
                S1_2 = string1[k]
                a.append(S1_2.lower())
                S2_2 = string2[k]
                a.append(S2_2.lower())
        Combinando = ''.join(str(x) for x in a)
        print(Combinando)

__Combinador__()