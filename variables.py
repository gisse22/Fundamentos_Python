# Define una variable de cada tipo de primitivo
nombre = "Gabriela"
edad = 40
mujer = True
estatura = 1.60

print("Variables \nNombre: ", nombre, "\nEdad: ", edad, "\nMujer: ", mujer, "\nEstatura: ", estatura)

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatenado = nombre + str(edad) + str(mujer) + str(estatura)
print("La concatenación de todas las variables es: ", concatenado)

""" 
Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
1. Python 3 utiliza enteros de precisión arbitraria, lo que significa que los enteros pueden ser tan grandes como la memoria disponible en tu sistema
2. los números de punto flotante en Python siguen el estándar IEEE 754 de precisión doble para la mayoría de las implementaciones. Esto significa que 
    los números de punto flotante de precisión doble (float64) tienen una precisión de aproximadamente 15-17 dígitos decimales significativos. 
    El rango de representación de números de punto flotante en Python es amplio, pero no infinito. El número más pequeño positivo representable en un 
    float64 es del orden de 1e-308, y el número más grande representable es del orden de 1e308.
"""

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = edad
suma = (n * (n + 1)) // 2 
print("La suma de los primeros", edad, "números pares es:", suma)

