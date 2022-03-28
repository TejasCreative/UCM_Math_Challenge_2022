drag = .5 #b
springconstant = 16 #k

def accerleration(x, velocity):
    return -drag*velocity-springconstant*x

t=0
x=0
velocity=1
dt= .0001

while t<10:
    x+=velocity*dt
    a=accerleration(x, velocity)
    velocity+=a*dt
    print("%.8f"%x)
    t+=dt
