
G = 9.8
friccion = input("Hay friccion en la simulacion?: ")
masa = float(input("Ingrese la masa del objeto: "))
fuerza = float(input("Ingrese la fuerza: "))
peso = masa*G


if friccion.lower() == "s":
    ue = float(input("Ingrese el mu estatico: "))
    ud = float(input("Ingrese el mu dinamico: "))
    ffe = peso*ue
    ffd = peso*ud
    if ffe < fuerza:
        print(f"El objeto se mueve a {(fuerza-ffd)/masa}m/s2")
    else:
        print(f"Se necesitan {ffe}N para mover el objeto")
else:
    if fuerza != 0:
        print(f"El objeto se mueve a {fuerza/masa}m/s2")
    else:
            print("Se necesita una fuerza mayor a 0 para mover el objeto.")