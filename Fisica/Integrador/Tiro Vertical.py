
G = 9.8

def hmax_v0():
    v0 = float(input("Ingrese la velocidad inicial: "))
    hmax = (v0**2)/(2*G)
    print(hmax)

def v0_hmax():
    hmax = float(input("Ingrese la altura maxima: "))
    v0 = (2*G*hmax)**(1./2.)
    print(v0)

def t_v0():
    v0 = float(input("Ingrese la velocidad inicial: "))
    t = v0/G
    print(t)

'''
Con esas 3 formulas se puede calcular todo.
'''