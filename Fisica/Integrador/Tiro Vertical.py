
from matplotlib import pyplot as plt
import numpy as np

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

def v0_t():
    t = float(input("Cuanto tiempo tarda en car el objeto"))
    v0 = G*(t/2)
    t /= 2
    print(v0)

def h_t():
    v0 = float(input("Ingrese la velocidad inicial: "))
    t = float(input("Ingrese el tiempo en q quiere saber la altura del objeto: "))
    h = v0*t+(0.5*-abs(G))*t**2
    print(h)

#Hmax 40m/s2 = 80m
def graphic_ht():
    v0 = float(input("Ingrese la velocidad inicial: "))
    t = int((v0/G)*2)
    h = lambda time : v0*time+(0.5*-abs(G))*time**2
    x = []
    y = []
    for i in range(t+1):
        x.append(i)
        y.append(h(i))
    x.append((v0/G)*2)
    y.append(0)
    plt.plot(x, y)
    plt.show()

graphic_ht()