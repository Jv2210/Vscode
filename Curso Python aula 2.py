#variaveis
numero1= 10
numero2= 5.5

#(como verificar a classe do numero, adicionando o - type - a frente da variavel ele mostra 
# se é um numero tipo int = inteiro ou tipo float = tipo decimal)

print (type(numero1))
print (type(numero2))

# para mudar a classe do numero só basta adicionar int ou float a frente do numero

(float(numero1))
(int(numero2))

#operadores aritiméticos
(numero1 + numero2) # soma 
(numero1 - numero2) # subtração
(numero1 * numero2) # multiplicação
(numero1 ** numero2)# exponenciação
(numero1 / numero2) # divisão
(numero1 // numero2)# divisão inteira
(numero1 % numero2) # resto da divisão

#funções extras
print (abs(-27)) # abs = transforma em número positivo
print (pow(6,3)) # pow = exponenciação
print (max(18,24,-33,64)) # max = maior número 
print (min(18,24,-33,64)) # min = menor número
print (round(9.7)) # round = arredonda o número a partir do 5, ou para baixo ou para cima

import math # usando a biblioteca de matemática 

print(math.floor(4.9)) # floor = sempre arredonta para baixo
print(math.ceil(4.1))  # ceil = sempre arredonda para cima
