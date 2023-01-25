#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

invertir = float(input("¿Cuanto dinero desea invertir? "))
interes = float(input("¿Interes por año? "))
tiempo = int(input("¿años?"))

print("Capital final: " + str(round(invertir * (interes / 100 + 1) ** tiempo, 2)))