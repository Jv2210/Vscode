# Collections, Lists, tuples

# Para fazer uma lista é necessário colocar entre colchetes "[]".
familia = ["Sandra", "Assis", "João", "Fabio"] 
#             0         1        2       3

print (familia[3]) # sempre começando do zero a contagem das variáveis. 
print (familia[-2]) # puxando de trás para frente as variáveis.
print (familia [1:]) # puxando a partir de uma variável. 
print (familia [0:3]) # mostra as variáveis de 0 a 2 pois o número 3 não conta.

familia[2] = "Lima" # aqui conseguimos trocar as variáveis.
print (familia)

familia.extend(["Socorro", "Juliana", "Maya"])# extend para adicionar lista a variável.
print (familia)

familia.append("Tia Lena")# para adicionar apenas um dado.
print(familia)

familia.insert(2,"Belinha")# para adicionar um dado na posição que desejo.
print(familia)

familia.pop()# para remover o ultimo dado da variável.
print(familia)

familia.remove("Juliana")# para remover um dado em especifico.
print(familia)

#familia.clear# para limpar todos os dados da variável.

print(familia.index("Fabio"))# mostrar a posição do dado pedido.

print(familia.count ("Assis"))# mostrar quantos dados iguais existem.

idade_familia = [66, 66, 7, 24, 39, 74, 8]
print (idade_familia)

idade_familia.sort()# deixar em ordem crescente, funciona string e números também.
print(idade_familia)

idade_familia.reverse()# para deixar a lista ao inverso, para deixar decrescente, primeiro adicionar o sort e depois o reverse.

print(idade_familia)

familia2 = familia.copy # para criar uma copia sem mudar as variáveis
familia.remove ("Sandra")
print(familia)
print(familia2)