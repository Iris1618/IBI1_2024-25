import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
y = re.findall(r'GT.*?AG', seq)
largest = max(y, key=len)
print("Longest intron:", largest)
print("Length:", len(largest))