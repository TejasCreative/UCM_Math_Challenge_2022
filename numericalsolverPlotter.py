import matplotlib.pyplot as plt
import numpy as np

def acc(x, velocity,drag, springconstant):
    return -drag*velocity-springconstant*x
def solve(x,v,b,k):
    t=0
    points = []
    while t<10:
        x += v*dt
        v += acc(x,v,b,k) * dt
        points.append(x)
        t+=dt
    return points
def overdamped(t,drag,k):
    r=np.sqrt(np.abs(drag**2-4*k))
    return 1/r * np.exp((-drag/2+r/2)*t)-1/r*np.exp((-drag/2-r/2)*t)
def criticaldamp(t,drag,k):
    r=np.sqrt(np.abs(drag**2-4*k))
    return t*np.exp((-drag/2)*t)
def underdamped(t,drag,k):
    r=np.sqrt(np.abs(drag**2-4*k))
    return 2/r * np.exp((-drag/2)*t)*np.sin(r/2*t)

dt = 1/8
time = list(np.linspace(0,10,80, endpoint=True))

plt.plot(time,solve(0,1,1,8), color='g', label='underdamp') 
plt.plot(time,solve(0,1,1,1/8), color='r', label='overdamp')
plt.plot(time, solve(0,1,1,.25), color='b', label='criticalDamp')

# overdampeddata = [overdamped(t,1,1/8) for t in time]
# criticaldampdata = [criticaldamp(t,1,.25) for t in time]
# underdampeddata = [underdamped(t,1,8) for t in time]

# plt.plot(time,overdampeddata, color='r', label='overdamp')
# plt.plot(time, criticaldampdata, color='b', label='criticalDamp')
# plt.plot(time,underdampeddata, color='g', label='underdamp') 

# plt.plot(time,list(np.abs(np.subtract(solve(0,0,1,1,1/8),overdampeddata))), color='r', label='overdamp')
# plt.plot(time, list(np.abs(np.subtract(solve(0,0,1,1,.25),criticaldampdata))), color='b', label='criticalDamp') 
# plt.plot(time, list(np.abs(np.subtract(solve(0,0,1,1,8),underdampeddata))), color='g', label='underdamp') 

plt.legend()
plt.title("Position of Oscillation with Respect to time")
#plt.title("Absolute error between Exact function and Numerical Approximation")
plt.xlabel("Time (s)")
#plt.ylabel("Error")
plt.ylabel("Position (m)")
plt.show()