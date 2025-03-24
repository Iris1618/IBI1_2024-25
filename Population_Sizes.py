# Define data for UK countries and Chinese provinces
# Print sorted data
# import matplotlib.pyplot
# create colormap
# Generate colors for UK pie char
# Create and display UK pie chart
# Generate colors for China pie chart
# Create and display China pie chart

uk_countries=[57.11,3.13,1.91,5.45]                #data definition
china_provinces=[65.77,41.88,45.28,61.27,85.15]   
labels_uk=['England', 'Wales', 'Northern Ireland','Scotland'] 
labels_china=['Zhejiang','Fujian', 'Jiangxi', 'Anhui','Jiangsu']
print(sorted(uk_countries))      #printing sorted data
print(sorted(china_provinces))
import matplotlib.pyplot as plt  #library imports
import numpy as np
cmap = plt.cm.tab20c      #colormap creation learned from internet
colors1= cmap(np.linspace(0, 1, len(labels_uk)))  #color generation
p1=plt.pie(uk_countries, labels=labels_uk,colors=colors1,autopct='%1.1f%%',shadow=False) #generate UK pie chart
plt.axis('equal')
plt.show()     #display chart
colors2 = cmap(np.linspace(0, 1, len(labels_china)))
p2=plt.pie(china_provinces,colors=colors2, labels=labels_china,autopct='%1.1f%%',shadow=False) #generate China pie chart
plt.axis('equal')
plt.show()  #display chart