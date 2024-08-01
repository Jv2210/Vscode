print("Sistema de calculo de imc")
#pedir a altura 
altura = float(input('Digite sua altura (m):'))
#Pedir o peso 
peso = float(input('Digite seu peso (kg):')) 

#Calcular o IMC -> Peso / altura²
imc = peso / (altura*altura)

print ("IMC: ", imc)
 
if imc <= 18.5: 
    print("Baixo Peso")
elif imc > 18.5 and imc < 25:
    print("Peso normal")
elif imc > 25 and imc < 29.9:
    print("está no sobrepeso") 
elif imc > 30 and imc < 34.9:    
    print ("está com obesidade grau 1")
elif imc > 35 and imc < 39.9:
    print ("está com obesidade grau 2")
else :
    print ("está com obesidade grau 3")




