import time 

# Es perfectamente posible llamar una función dentro de otra
# Lo hicimos cuando calculamos el volumen de un cilindro.

# Pero también es perfectamente posible que una funcion se llame a si misma
# Esto es una técnica muy poderosa para cierto problemas

# Función conteo regresivo 
# Es una funcion que se llama a si misma
def countdown(number):
    if number <=0:
        print("KABUMM!")
    else:
         print(number)
         time.sleep(0.5)
         countdown(number -1)

countdown(5)

# Otro ejemplo para hacer una sumatoria
def super_sum(number):
    if number <= 0:
        return number
    else:
        return number + super_sum(number - 1)

print(super_sum(3))

# Recursión infinita, sin condición de salida 
# Para nada útil, pero entretenida 
def infinite():
    infinite()

infinite()