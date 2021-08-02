import numpy as np
import random
import matplotlib.pyplot as plt

N_steps = 10**5
N_brownians = 10**0
stepsize = 10**-5

x = np.zeros([N_steps, N_brownians])
t = np.linspace(0,N_steps, N_steps)

for jndex in range(N_brownians):
    for index in range(N_steps-1):
        random_number = random.uniform(0, 1)

        if round(random_number) == 0:
            x[index+1, jndex] = x[index,jndex] + stepsize
        elif round(random_number) == 1:
            x[index+1, jndex] = x[index,jndex] - stepsize

np.savetxt('brownian_motion.csv', x, delimiter=',')

plt.figure(1)
plt.plot(t, x )
plt.xlabel('Timesteps')
plt.ylabel('Displacement')
plt.show()