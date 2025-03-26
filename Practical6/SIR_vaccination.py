import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def sir_model(N, V_rate, beta, gamma, times):
    V = int(N * V_rate)
    N=10000
    S=N-V-1
    I=1
    R=0
    S=max(S,0)
    I_array=[]
    I_array.append(I)
    
    for i in range(times):
        infection_p=beta*I/N
        new_I = np.random.choice(range(2), S, p=[1 - infection_p, infection_p]).sum()
        new_R=np.random.choice(range(2),I,p=[1-gamma,gamma]).sum()
        
        S -= new_I
        S=max(S,0)
        I = I+ new_I - new_R
        I=max(I,0)
        R += new_R
        R=max(R,0)
        I_array.append(I)
    return I_array

V_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
I_data = []
N=10000
times=1000
beta=0.3
gamma=0.05

for rate in V_rate:
    I_array = sir_model(N, rate,beta,gamma,times)
    I_data.append(I_array)

plt.figure(figsize=(6, 4), dpi=150)

for i in range(len(V_rate)):
    plt.plot(I_data[i], color=cm.plasma(148), label=f'{int(V_rate[i]*100)}%')

plt.xlabel('time')
plt.ylabel('number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()
