w=int(input("please enter your weight _kg:"))
h=float(input("please enter your height_m:"))
bmi=w/h   #caculate bmi
if bmi>30:             #compare
    print("obese")
elif bmi<18.5:
    print("underweight")
else:
    print("normal")