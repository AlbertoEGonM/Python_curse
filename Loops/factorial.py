#El factorial es una operación matemática.

#El factorial de n es el producto de todos los enteros positivos menores o iguales a n.

# 1. Lee una entrada entera
numero = int(input())

# 2. Inicializa una variable de resultado a 1
factorial = 1

# Manejar los casos especiales para 0 y 1.
# El bucle for range(1, numero + 1) ya maneja el caso de numero = 0,
# donde el bucle no se ejecuta y factorial sigue siendo 1.
# Sin embargo, si quieres una estructura más clara:

if numero < 0:
    # Aunque el enunciado solo pide manejar enteros no negativos,
    # es buena práctica considerarlo.
    # En este contexto, simplemente asumiremos que la entrada será no negativa.
    # Pero para n >= 0:

    pass # No hacemos nada si es no negativo, continuamos con el cálculo.

elif numero == 0 or numero == 1:
    # El factorial de 0 y 1 es 1.
    factorial = 1

else:
    # 3. Usa un bucle para multiplicar todos los números desde 1 hasta el número de entrada
    for i in range(1, numero + 1):
        factorial = factorial * i

# 4. Imprime el resultado final (solo el número, sin texto adicional)
print(factorial)