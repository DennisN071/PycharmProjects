import numpy as np
import random
import matplotlib.pyplot as plt

N_steps = 10**2
stepsize = 10**-5

x = np.zeros(N_steps)
y = np.zeros(N_steps)
dx = np.zeros(N_steps)
t = np.linspace(0,N_steps, N_steps)

for index in range(N_steps-1):

    random_number = random.uniform(0, 1)

    if round(random_number) == 0:
        x[index+1] = x[index] + stepsize
    elif round(random_number) == 1:
        x[index+1] = x[index] - stepsize

    dx[index] = x[index+1]-x[index]

    if x[index] == 0:
        y[index] = 0
    else:
        y[index] = dx[index]/x[index]

plt.figure(1)
plt.plot(t, x)
plt.plot(t, y/10**20)
plt.xlabel('Timesteps')
plt.ylabel('Displacement')
plt.show()
