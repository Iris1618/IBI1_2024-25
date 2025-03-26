#Create a matrix to represent the population
#Initialize all cells to 0 
#Randomly select an outbreak location and set it to 1 
#Set parameters: infection probability (beta), recovery probability (gamma), number of time steps (times)

#Function to find infected cells in the population
#Function to determine neighboring cells for a given cell
#Function to infect neighboring cells based on probability
#Function to check recovery of infected cells based on probability

#For each time step from 0 to times:
#Find all currently infected cells
#Create a copy of the current population state
#For each infected cell: Identify all neighboring cells
#Infect neighboring cells
#Recover cells
#Update the population matrix with new states

#Display the initial population grid
#After simulation completes, display the final population grid
#Add a color bar to indicate the meaning of each color

import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
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
plt.show()