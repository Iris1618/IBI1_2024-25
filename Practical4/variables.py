a=15
b=75
c=a+b
d=90
e=5
f=d+e
if c>f:
    print("car-based commute faster")
elif c<f:
    print("bus-based commute faster")
else:
    print("equal")
X=True
Y=False
W= X and Y
print(W)
# truth table of W:
#   X  |   Y  |  W
# True | True | True  
# True | False| False 
# False| True | False  
# False| False| False