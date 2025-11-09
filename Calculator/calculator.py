#En este proyecto, crearás un programa simple que calcula cuánto debe pagar cada persona, incluyendo la propina.
#Todo buen programa comienza con un mensaje de bienvenida, muestra en pantalla la siguiente cadena:
print("¡Bienvenido a la calculadora de propinas!")
#Después del mensaje de bienvenida, obtén dos números (float) del usuario que indiquen el monto de la factura y el porcentaje de propina, en ese orden.
print("¿Cuál es el monto de la factura?")
fact = input()
print("¿Cuál es el porcentaje de propina que te gustaría dar?")
tip_por = input()



#Obtén el porcentaje de propina de la entrada del usuario
fact = float(fact)
tip_por = float(tip_por)
#Calcula la propina y el total de la factura
tip = (tip_por / 100)*fact

total = float()
total = tip + fact

print(f"{total}")

#Finalmente, obtén un número entero del usuario que indique cuántas personas dividirán la factura (incluida la propina).
print("¿Cuántas personas dividirán la factura?")
num_per = input()
num_per = int(num_per)
total_por_persona = float()
total_por_persona = total / num_per

print(f"{total_por_persona}")

#¡El último paso de este proyecto es formatear la salida!
total_por_persona = "{:.2f}".format(total_por_persona)
#Usa f-strings para mostrar a cada persona cuánto debe pagar. Asegúrate de que el resultado final tenga dos decimales.
print(f"Cada persona debe pagar: ${total_por_persona}")