"""
    ***************************************************************************************************************************
    *                                                                                                                         *  
    *    Durante anos, todos os contratos da Associação de Contratos da Modernolândia (ACM)                                   *  
    *    foram datilografados em uma velha máquina de datilografia.                                                           *      
    *    Recentemente Sr. Miranda, um dos contadores da ACM, percebeu que a máquina apresentava                               *          
    *    falha em um, e apenas um, dos dígitos numéricos. Mais especificamente, o dígito falho,                               *  
    *    quando datilografado, não é impresso na folha, como se a tecla correspondente não tivesse sido pressionada.          *  
    *   Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e,                        *  
    *    preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos,                 *  
    *    que ele mantinha em anotações manuscritas, quais os valores de fato representados nos contratos.                     *  
    *    Por exemplo, se a máquina apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato                  *  
    *    como 100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor numérico representado               *  
    *    no contrato, ou seja, nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000                  *  
    *    (como ele de fato aparece impresso).                                                                                 *  
    *                                                                                                                         *  
    *    Entrada                                                                                                              *  
    *    A entrada consiste de diversos casos de teste, cada um em uma linha. Cada linha contém dois inteiros D e N           *
    *    (1 ≤ D ≤ 9, 1 ≤ N < 10100 ),                                                                                         *  
    *    representando, respectivamente, o dígito que está apresentando problema na máquina e o número que foi negociado      *
    *    originalmente no contrato (que podem ser grande, pois Modernolândia tem sido acometida por hiperinflação nas         *  
    *    últimas décadas).                                                                                                    *          
    *                                                                                                                         *      
    ***************************************************************************************************************************
"""
def NumberBroken():
    Num_quebrado = int(input("Digite o numero quebrado: "))

    if Num_quebrado >= 1 and Num_quebrado < 11:
        Num_Contrato = int(input("Digite numero do contrato: "))
        if Num_Contrato > 0 and Num_Contrato < 10100:
            Quebrado = str(Num_Contrato).replace(str(Num_quebrado), '')
            print(Quebrado)
        if Num_Contrato == 0:
            print('0')


NumberBroken()