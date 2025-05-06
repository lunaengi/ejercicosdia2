#Esta en la lista de invitados?
#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
# Pide al usuario su nombre.
# Usa ifpara decir si está en la lista de invitados o no.

invitados  = ["liz","sofi","stiv","sandra","carlos"]

buscar = input("cual estu nombre?")

if buscar in invitados :
    posicion= invitados.index(buscar)
    print(f"el invitado {buscar} esta en la lista de invitados")
else:
    print(f"el invitado { buscar} no esta en la lista")
