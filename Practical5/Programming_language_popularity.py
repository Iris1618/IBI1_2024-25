#Define a dictionary with programming languages and their popularity percentages
#Print the dictionary use print()
#Import matplotlib
#Extract keys and values from the dictionary
#Create a bar chart using matplotlib
#Add title and labels to the chart
#set title to "Programming language popularity"
#set y-axis label to "language"
#set x-axis label to "percentage"
#show the chart

d={'JavaScript' :62.3, 'HTML': 52.9,'Python':51, 'SQL': 51, 'TypeScript': 38.5 }  #dictionary defination
print(d)                        # print the dictionary
import matplotlib.pyplot as plt #import necessary library
c = list(d.keys())              #data extraction
v = list(d.values())
p1=plt.bar(c,v,color='skyblue')                 #bar chart creation
plt.title("Programming language popularity")
plt.ylabel("language")
plt.xlabel("percentage")
plt.show()                      # show chart
print(d['Python'])              # print designated popularity