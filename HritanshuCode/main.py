import matplotlib.pyplot as plt

drag = 1 #b
springconstant = 0.25 #k
accuracy = 10000

def acc(x, velocity):
    return -drag*velocity-springconstant*x

t = 0
x = 0
v = 1
a = 0
dt = 1/accuracy
time = []
points = []

while t<10:
    x += v*dt
    v += a * dt
    a = acc(x, v)
    #print("%.8f"%x)
    points.append(x)
    time.append(t)
    t+=dt

plt.plot(time, points, color='b', label='criticalDamp') #------------------------------------
t = 0
x = 0
v = 1
a = 0

points = []
springconstant = 8
while t<10:
    x += v*dt
    v += a * dt
    a = acc(x, v)
    #print("%.8f"%x)
    points.append(x)
    t+=dt

plt.plot(time, points, color='g', label='underdamp') #--------------------------------------

t = 0
x = 0
v = 1
a = 0
points = []
springconstant = 1/8
while t < 10:
    x += v * dt
    v += a * dt
    a = acc(x, v)
    # print("%.8f"%x)
    points.append(x)
    t += dt

plt.plot(time, points, color='r', label='overdamp')  # --------------------------------------
plt.legend()
plt.title("Position of Spring Oscillation in Respect to Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.show()


