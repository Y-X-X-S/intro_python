# Los arreglos son una ESTRUCTURA DE DATOS FUNDAMENTAL 
# que permite agrupar valores, separados por coma  

firts_array = ['Sacar la basura','peinarse','dormir','Sacar la ropa']

# En python el primer elemento de un elemento tiene posicion (índice) 0
print(firts_array [0])
print(firts_array [1])
print(firts_array [2])
print(firts_array [3])
# No esxiste el elemento con indice 4 y python da un error 
# print(firts_array [4])

# Podemos saber el largo de un arreglo o lista con la función pre definida len()
print(len(firts_array))

# Ademas, podemos agregar elementos al final de arreglo con el metodo append
firts_array.append('comer')
firts_array.append('Dormir')

# Podemos indicar la posicion del nuevo elemento a agregar con insert 
firts_array.insert(0,'Levantarse')

#Podemos imprimir la lista completa 
print(firts_array)