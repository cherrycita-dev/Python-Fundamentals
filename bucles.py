""""
    Ejemplo de for

frutas = ["manzana", "banana", "naranja"] #Secuencia


for fruta in frutas:
    print(fruta)


    Ejemplo de while
contador = 0

while contador < 5:

    print(contador)
    contador += 1
    

#Usar for para imprimir una secuencia de numeros (1,5) multiplicado por 2

print("Numeros del 1 al 5 multiplicados por dos")
for numero in range (1 , 6):
    print(numero*2)

Usando while    
contador=1

while contador<=5:
    print(contador*2)
    contador +=1



for i in range(10):

    if i % 2 == 0:
        continue
    print(i)      
#Imprime los numeros impares     

    """

for i in range(5):
    pass
