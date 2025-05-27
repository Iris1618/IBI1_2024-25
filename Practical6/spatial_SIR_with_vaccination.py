import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
V_rate = float(input("please input the vaccination rate:"))
V = np.random.choice(range(100), int( 100 * V_rate), replace=False)
for x in V:
    while True:
        y = np.random.choice(range(100))
        if population[x, y] == 0:  #Avoid repeated vaccinations
            population[x, y] = 3
            break

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
                population[nx,ny]=np.random.choice([1,2],1,p=[1-beta,beta])
def recover(x, y):
    population[x,y]=np.random.choice([1,2],p=[1-gamma,gamma])

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
    if t==10 or t==50 or t==99:
        population=new_population
        plt.figure(figsize=(10, 10), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.colorbar(ticks=[0,1,2,3],label="State(0=Susceptible, 1=Infected, 2=Recovered, 3=Vaccinated)") 
plt.show()

