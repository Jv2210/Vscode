#pedir a temperatura em celsius
temp_celsius = float(input('digite a temperatura em celsius:'))
print (temp_celsius)
print(type(temp_celsius))
#fazendo o calculo de temp celsius para fahrenheint
temp_fahren = temp_celsius * 1.8 + 32
print("A temperatura em celsius de)",
temp_celsius, "é de", temp_fahren,"fahrenheit")