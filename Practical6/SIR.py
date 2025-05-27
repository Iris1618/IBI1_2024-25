import numpy as np
import matplotlib.pyplot as plt
N=10000
S=N-1
I=1
R=0
times=1000
beta=0.3
gamma=0.05
S_array=[]
S_array.append(S)
I_array=[]
I_array.append(I)
R_array=[]
R_array.append(R)
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
    
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_array, label='susceptible')
plt.plot(I_array, label='infected')
plt.plot(R_array, label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.grid(True)
plt.savefig('SIR_model.png')
plt.show()