import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
y= re.findall(r'GT.+AG',seq)
print(y)
print(len(y[0]))