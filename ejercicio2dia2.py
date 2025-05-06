#2. Verificar si un número está en una lista
#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista de la lista in.

numeros = [45,76,88,91,63]
buscar =int(input("¿que numero buscas?"))
 
if buscar in numeros :
    posicion = numeros.index(buscar)
    print(f"el numero {buscar} esta en {posicion}")
else :
    print(f"el numero {buscar} no se encuentra el la lista")
