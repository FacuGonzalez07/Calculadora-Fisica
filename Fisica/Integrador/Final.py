import matplotlib as mpl


G = 9.8
def main():
    print("1_Tiro Vertical\n2_Caida Libre\n3_Movimiento Plano\n4_Tiro Oblicuo.")
    ejecicio = input("\nQue ejercicio quiere hacer: ")

    if ejecicio == "1":
        tiro_vertical()
    elif ejecicio == "2":
        print(2)
    elif ejecicio == "3":
        print(3)
    elif ejecicio == "4":
        print(4)
    else:
        print("\nIngrese la posicion de un ejercicio valido")

def caida_libre():
    
    pass

def tiro_vertical():
    print("\n1_Velocidad Inicial\n2_Altura maxima\n3_Tiempo en Caer")
    datos = input("\nQue datos desea ingresar: ")
    if datos == "1":
        v0 = float(input("\nIngrese la velocidad inicial: "))
        hmax = (v0**2)/(2*G)
        t = v0/G
    elif datos == "2":
        hmax = float(input("\nIngrese la altura maxima: "))
        v0 = (2*G*hmax)**(1./2.)
        t = v0/G
    elif datos == "3":
        t = float(input("Cuanto tiempo tarda en car el objeto"))
        v0 = G*(t/2)
        hmax = (v0**2)/(2*G)
        t = t/2
    else:print("\nIngrese una respuesta valida")
    print(f"\nLa altura maxima es de {hmax}m\nLa velocidad Inicial es de {v0}m/s2\nEl tiempo que tarda en llegar a la altura maxima {t}s\nEl tiempo que tarda en caer el objeto es de {t*2}s")
    x = [t]
    y = []

main()