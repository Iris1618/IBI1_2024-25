class patients:
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name=name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
    def details(self):
        return(f"Patient Name: {self.name}, Age: {self.age}, Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")

name= "Iris" 
age="18"
date_of_latest_admission="2025.1.21"
medical_history="rhinitis"
patient1= patients(name,age,date_of_latest_admission,medical_history)
print(patient1.details())