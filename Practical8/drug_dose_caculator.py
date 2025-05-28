def drug_dose_calculator(weight, strength_of_paracetamol):
    r=15
    weight=int(weight)
    strength=int(strength_of_paracetamol)
    if not(10<int(weight)<100):
        return "weight out of range(10-100kg)"
    if strength not in [120,250]:
        return "invalid strength"
    volume=r*weight/strength*5
    return f"{volume:.2f}ml"
weight=input("Please input the weight of children up to 18:")
strength_of_paracetamol=input("Please input the strength of paracetamol(120mg/5ml or 250mg/5ml)--120 or 250 ")
print(drug_dose_calculator(weight, strength_of_paracetamol))