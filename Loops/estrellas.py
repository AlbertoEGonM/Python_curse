#Escribe código que imprima un patrón rectangular de estrellas (*) usando bucles anidados.

#Tu programa debería:

#Leer dos enteros: rows y cols
#Usar una estructura de bucles anidados para imprimir el patrón
#El bucle exterior debería iterar a través de cada fila
#El bucle interior debería construir cada fila con el número correcto de estrellas
#Imprimir cada fila completada
#Ejemplo: si la entrada es 3 filas y 4 columnas, la salida debería ser:

#****
#****
#****

# Obtener entrada para filas y columnas
rows = int(input())
cols = int(input())

# Escribe tus bucles anidados aquí
# Bucle exterior para filas
for i in range(rows):
    line = ""
# Bucle interior para columnas
    for j in range(cols):
        line += "*"
    print(line)