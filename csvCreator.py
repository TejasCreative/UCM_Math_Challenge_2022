import csv

f=open('x.csv','w')

writer = csv.writer(f)



drag = .5 #b
springconstant = 16 #k

def accerleration(x, velocity):
    return -drag*velocity-springconstant*x

t=0
x=0
velocity=1
dt= .0001

tList = []

while t<10:
    x+=velocity*dt
    velocity+=accerleration(x, velocity)*dt
    print(t)
    tList.append("%.4f"%t)

    


    t+=dt
writer.writerow(tList)
f.close()