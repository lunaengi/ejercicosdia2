#Edad
# Pide al usuario su edad.
#Si la edad es menor que 0 o alcalde que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

edad= int(input("digita tu edad: "))

if edad < 0 or edad > 120 :
    print("la edad no es valida")
else :
    print("edad valida")