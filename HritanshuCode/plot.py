import matplotlib.pyplot as plt

dt = 0.0001
t = 0
time = []
position = []

f = open("criticaldamp.txt", 'r')
for row in f:
    #position.append(row)
    print(row)
f.close()

while t < 10:
    time.append(t)
    t+=dt

plt.title("Critically Damped")
plt.plot(time, position)
plt.show()
'''
file = open("underdamp.txt", 'r')
for row in file:
    position.append(row)
file.close()

plt.title("Under Damped")
plt.plot(time, position)
plt.show()

file = open("overdamp.txt", 'r')
for row in file:
    position.append(row)
file.close()

plt.title("Over Damped")
plt.plot(time, position)
plt.show()
'''
