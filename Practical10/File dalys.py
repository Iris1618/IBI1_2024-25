import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('c:/Users/Iriss/Desktop/IBI')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print('the year for the first 10 rows\n',dalys_data.iloc[0:10,2])
dalys_sort=dalys_data[dalys_data['Entity']== 'Afghanistan'].sort_values(by='Year',axis=0, ascending=True)
print('the 10th year with DALYs data recorded in Afghanistan\n', dalys_sort.iloc[9,2])

year=[]
for i in range(len(dalys_data)):
    if dalys_data.loc[i,'Year']==1990:
        year.append(True)
    else:
        year.append(False)
print('DALYs for all countries in 1990\n',dalys_data.loc[year,'DALYs'])

uk_mean=dalys_data.loc[dalys_data['Entity']=='United Kingdom','DALYs'].mean()
france_mean=dalys_data.loc[dalys_data['Entity']=='France','DALYs'].mean()
print('the mean DALYs in the UK: ', uk_mean)
print('the mean DALYs in the France: ',france_mean)
if uk_mean>france_mean:
    print('the mean DALYs in the UK was greater than France')
elif uk_mean==france_mean:
    print('the mean DALYs in the UK was equal to France')
else:
    print('the mean DALYs in the UK was greater than France')
    
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.title('the DALYS over time in the UK')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()

china=dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
merge_df=pd.merge(uk, china,on='Year',suffixes=('_uk','_china'))
merge_df['absolute_difference']=abs(merge_df['DALYs_china']-merge_df['DALYs_uk'])
print(merge_df)
plt.plot(merge_df['Year'], merge_df['absolute_difference'], 'r+')
plt.xticks(merge_df['Year'],rotation=-90)
plt.title('the absolute difference of DALYs between China and UK')
plt.xlabel("Years")
plt.ylabel("absolute difference of DALYs")
plt.show()