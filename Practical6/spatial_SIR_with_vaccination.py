import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
V_rate = float(input("please input the vaccination rate:"))
V = np.random.choice(range(100), int( 100 * V_rate), replace=False)
for x in V:
    y = np.random.choice(range(100))
    population[x, y] = 3
outbreak=np.random.choice(range(100),2)
while population[outbreak[0],outbreak[1]]==3:
    outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

def find_infected(population):
    return np.where(population == 1)

def address_neighbors(x, y):
    neighbors = []
    d=[-1,0,1]
    for dx in d:
        for dy in d:
            if dx == 0 and dy == 0:
                continue  
            neighbors_x = x + dx
            neighbors_y = y + dy
            if 0 <= neighbors_x <100 and 0 <= neighbors_y <100:
                neighbors.append((neighbors_x, neighbors_y))
    return neighbors

def infect_neighbors(neighbors):
    for nx, ny in neighbors:
            if population[nx, ny] == 0:        
                if np.random.rand() < beta:
                    population[nx, ny] = 1     # Infect
                    #population[nx,ny]=np.random.choice(range(2),1,[1-beta,beta]) why cannot

def recover(x, y):
    if np.random.rand() < gamma:
        population[x, y] = 2   #population[x,y]=np.random.choice(range(2),1,[1-gamma,gamma])

beta=0.3
gamma=0.05
times=100
for t in range(times):
    infected_x, infected_y=find_infected(population)
    new_population=population
    for i in range(len(infected_x)):
        x=infected_x[i]
        y=infected_y[i]
        neighbors = address_neighbors(x, y)
        infect_neighbors(neighbors)
        recover(x,y)

population=new_population
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.colorbar(ticks=[0,1,2,3],label="state") # 0 for susceptible\1 for infeted\2 for recovered\3 for vaccinated
plt.show()