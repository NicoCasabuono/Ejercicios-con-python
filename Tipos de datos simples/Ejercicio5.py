#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
precioXhora = 10
horasTrabajadas = int(input("Introdusca cantidad de horas trabajadas:"))

print(f"La cantidad de horas trabajadas es: {horasTrabajadas} \nEl pago del dia de hoy es: ", horasTrabajadas*precioXhora)
