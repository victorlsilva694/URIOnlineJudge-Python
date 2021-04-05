
"""
    ****************************************************************************************************************
    * Textos podem conter mensagens ocultas. Neste problema a mensagem oculta em um texto é composto               * 
    * pelas primeiras letras de cada palavra do texto, na ordem em que aparecem.                                   *  
    *                                                                                                              *  
    * É dado um texto composto apenas por letras minúsculas ou espaços. Pode haver mais de um espaço               *  
    * entre as palavras. O texto pode iniciar ou terminar em espaços, ou mesmo conter somente espaços.             *     
    *                                                                                                              * 
    * Entrada:                                                                                                     *  
    *                                                                                                              *         
    * A entrada contém vários casos de testes. A primeira linha de entrada contém um inteiro N que indica a        * 
    * quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de uma única linha contendo       *  
    * de um a 50 caracteres, formado por letras minúsculas (‘a’-‘z’) ou espaços (‘ ’). Atenção para possíveis      * 
    * espaços no início ou no final do texto!                                                                      * 
    *                                                                                                              * 
    * Saída                                                                                                        *     
    *                                                                                                              *
    * Para cada caso de teste imprima a mensagem oculta no texto de entrada.                                       * 
    ****************************************************************************************************************



"""

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