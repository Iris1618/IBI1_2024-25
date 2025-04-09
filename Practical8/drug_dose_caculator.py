def drug_dose_caculator(weight, strength_of_paracetamol):
    r=15
    if 10<int(weight)<100:
        return r*int(weight)/int(strength_of_paracetamol)*5
    else:
        return False
    
weight=input("Please input the weight of children up to 18:")
strength_of_paracetamol=input("Please input the strength of paracetamol(120mg/5ml or 250mg/5ml)--120 or 250 ")
print(drug_dose_caculator(weight, strength_of_paracetamol))