
from cmath import sin, pi

pendiente = str(input("Desea que el bloque se encuentre en una pendiente? s/n "))
masa = float(input("Ingrese la masa del objeto: "))

GRAVEDAD = 10
peso = masa * GRAVEDAD

def complex_float():
    global pesox
    global pesoy
    global ffe
    global ffd
    a=pesox_com.real
    b=pesox_com.imag
    c=pesoy_com.real
    d=pesoy_com.imag
    pesoy=c+d
    pesox=a+b
    ffe = ue*pesoy
    ffd = ud*pesoy

def print_datos():
    decimal(normal)
    print(f"La Normal es de {dec}N")
    decimal(pesoy)
    print(f"El peso en el eje y es de {dec}N")
    decimal(pesox)
    print(f"El peso en el eje x es de {dec}N")
    decimal(ffe)
    print(f"La fuerza de friccion estatica es de {dec}")
    decimal(ffd)
    print(f"La fuerza de friccion dinamica es de {dec}\n")
    
    if ffe > pesox:
        decimal(pesox/pesoy)
        print(f"El objeto no se mueve, la friccion es muy alta.\nPara que el objeto se mueva el μe tiene que ser {dec}")

    else:
        decimal((pesox-ffd)/masa)
        print(f"El objeto se mueve a una aceleracion de {dec} m/s")

def decimal(x):
    global dec
    dec = "{:.2f}".format(x)

if pendiente.lower() == "s":
    normal = peso
    print(
        '''
       A|\ 
        | \ 
        |  \ 
        |   \ 
        |    \ 
        |     \ 
        B------C
    '''
    )
    anguloa = float(input("Ingrese el angulo 'a': "))
    anguloc = float(input("Ingrese el angulo 'c': "))
    print(f"El angulo 'b' mide 90 grados")  
    pesox_com = (normal/sin((90*pi)/180))*sin((anguloc*pi)/180)
    pesoy_com = (normal/sin((90*pi)/180))*sin((anguloa*pi)/180)
    ue = float(input("Ingrese el mu estatico: "))
    ud = float(input("Ingrese el mu dinamico: "))
    ffe = peso*ue
    ffd = peso*ud
    complex_float()
    print_datos()

else:
    fuerza = float(input("Ingrese la fuerza: "))
    friccion = str(input("Hay friccion en la simulacion? s/n "))

    if friccion.lower() == "s":
        ue = float(input("Ingrese el mu estatico: "))
        ud = float(input("Ingrese el mu dinamico: "))
        ffe = peso*ue
        ffd = peso*ud
        if ffe < fuerza:
            semueve = True
            a_ms2 = (fuerza-ffd)/masa

        else:
            semueve = False
            decimal(ffe)
            f_mover = dec

    else:
        if fuerza != 0:
            semueve = True
            a_ms2 = fuerza/masa

        else:
            semueve = False
            f_mover = 0.01

    if semueve == True:
        decimal(a_ms2)
        print(f"El objeto se mueve a {dec} m/s2")

    else:
        print(f"El objeto no se mueve, se necesitan mas de {f_mover}N para mover el objeto")
