class Patient:
  def __init__(self,name,bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount
  def get_name(self):
    return self.__name
  def set_name(self):
    self.__name = name
  def get_bill_amount(self):
    return self.__bill_amount
  def set_bill_amount(self):
    self.__bill_amount = bill_amount
  def calculate_bill(self):
    return self.__bill_amount

class SeniorPatient(Patient):
  def calculate_bill(self):
    return self.get_bill_amount()*0.8

class PhilHealthPatient(Patient):
  def calculate_bill(self):
    return self.get_bill_amount()*0.85

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philHealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
for patient in [regular_patient, senior_patient, philHealth_patient]:
  print(f"Patient Name: {patient.get_name()}")
  print(f"Original Bill: {patient.get_bill_amount():,.2f}")
  print(f"Final Bill: {patient.calculate_bill():,.2f}\n")
