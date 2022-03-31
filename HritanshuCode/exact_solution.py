import matplotlib.pyplot as plt
import numpy as np

'''
Initializing
'''
damp_b = 1  # b
spring_k = 0.125    # k
disc = np.power(damp_b, 2) - 4*spring_k
discr = np.power(disc, 0.5)
t = 0
x = 0
v = 1
dt = 0.001

time = []
points = [] # initialized later
while t < 10:
    time.append(t)
    t+=dt

t = 0

# cases -----------------
'''
Equations
equation = 0
if disc < 0:
    equation = (2/np.power((-1)*disc, 0.5)) * np.power(np.e, (-1)*damp_b*t/2) * np.sin(np.power((-1)*disc, 0.5)*t/2)
if disc == 0:
    equation = t * np.power(np.e, (-1) * damp_b * t/2)
if disc > 0:
    equation = (1/discr) * np.power(np.e, (-1 * damp_b + discr) * t/2) - (1/discr) * np.power(np.e, (-1 * damp_b - discr) * t/2)
'''
# cases end -------------------


def d_l_z(x, v, t, dt):  # descriminant is less than 0
    point = []
    while t < 10:
        point.append((2/np.power((-1)*disc, 0.5)) * np.power(np.e, (-1)*damp_b*t/2) * np.sin(np.power((-1)*disc, 0.5)*t/2))
        t+=dt
    return point


def d_e_z(x, v, t, dt):  # d = 0
    point = []
    while t < 10:
        point.append(t * np.power(np.e, (-1) * damp_b * t/2))
        t+=dt
    return point


def d_g_z(x, v, t, dt):  # d > 0
    point = []
    while t < 10:
        point.append((1/discr) * np.power(np.e, (-1 * damp_b + discr) * t/2) - (1/discr) * np.power(np.e, (-1 * damp_b - discr) * t/2))
        t+=dt
    return point


def chk():
    if disc < 0:
        return d_l_z(0, 1, 0, dt)
    if disc == 0:
        return d_e_z(0, 1, 0, dt)
    if disc > 0:
        return d_g_z(0, 1, 0, dt)

# Numerical check ---------------------
def acc(x, velocity,springconstant):
    return -damp_b*velocity-springconstant*x

def solve(t,x,v,k):
    points = []
    while t<10:
        x += v*dt
        v += acc(x, v,k) * dt
        points.append(x)
        t+=dt
    return points


def subtract_list(list1, list2):
    i = 0
    list_return = []
    while i < len(list1):
        list_return.append(list1[i] - list2[i])
        i+=1
    return list_return


# print (len(time), " ", len(points))
# size error, so adding one end dt
'''
Plotting error
'''
points = chk()
points2 = solve(0,0,1,spring_k)
plt.plot(time, subtract_list(points, points2), color='g', label='overdamp')

spring_k = 0.25
disc = np.power(damp_b, 2) - 4*spring_k
discr = np.power(disc, 0.5)
points = chk()
points2 = solve(0,0,1,spring_k)
plt.plot(time, subtract_list(points, points2), color='b', label='critDamp')

spring_k = 8
disc = np.power(damp_b, 2) - 4*spring_k
points = chk()
points2 = solve(0,0,1,spring_k)
plt.plot(time,subtract_list(points, points2), color='r', label='underdamp')

plt.legend()
plt.show()
