w=int(input("please enter your weight _kg:")) # User input for weight in kilograms
h=float(input("please enter your height_m:")) # User input for height in meters
bmi=w/(h**2)  ## Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)
# Compare the calculated BMI to determine the category
if bmi>30:           # If BMI is greater than 30  
    print("obese")
elif bmi<18.5:       # If BMI is less than 18.5
    print("underweight")
else:                # If BMI is between 18.5 and 30
    print("normal")