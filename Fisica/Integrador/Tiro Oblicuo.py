
import cmath
import math

G = 9.8
v0 = float(input("Ingrese la velocidad inicial: "))
ang_out = float(input("Ingrese el angulo de salida: "))
x0 = float(input("Ingrese la pocicion inicial en x: "))
y0 = float(input("Ingrese la pocicion inicial en y: "))

v0x = v0*cmath.cos(math.radians(ang_out))
v0y = v0*cmath.sin(math.radians(ang_out))

t = -abs(v0y)/-abs(G)

xmax = x0+v0x*(t*2)

hmax = y0+v0y*t+0.5*-abs(G)*t**2