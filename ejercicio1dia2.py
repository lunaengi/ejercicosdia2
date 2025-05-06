numer1 = int (input("digite el primer número: "))
numer2 = int (input("digite el segundo número: "))
numer3 = int (input("digite el tercer número: "))


if numer2 < numer1:
    print (f"{numer2}es menor que {numer1}")

elif numer3 < numer2:
    print (f"{numer3}es menor que {numer2}")

elif numer1 < numer2:
    print(f"{numer1}es menor que {numer2}")

elif numer2 < numer3:
    print(f"{numer2}es menor que {numer3}")

elif numer3 < numer1:
    print (f"{numer3}es menor que {numer1}")

else:
    print (f"{numer1}es menor que {numer3}")



