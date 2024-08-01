print (input("digite o valor a sacar")); 

valor_a_sacar = 18
valor_em_conta = 20
valor_em_caixa = 20


condicao = valor_a_sacar <= valor_em_caixa
if condicao:
    print("primeira etapa okay, tem dinheiro em conta")
    if valor_a_sacar <= valor_em_caixa:
        print("saque realizado")
        valor_em_conta = valor_em_conta - valor_a_sacar
        print("valor atualizado com sucesso")
    else:
        print("valor em caixa insuficiente")
else:
    print ("saldo insuficiente")

print ("encerrando atendimento")
    