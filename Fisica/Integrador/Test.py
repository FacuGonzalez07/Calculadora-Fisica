from matplotlib.pyplot import *
from numpy import *
x=linspace(-1,5,3000)

y= x**3
plot(x, y)
xlabel("x axis")
ylabel("y axis")
print(x)
show()