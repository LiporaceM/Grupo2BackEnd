import pydicom
ds = pydicom.dcmread("C:/Users/Matheus/Desktop/ibmec/Grupo2BackEnd/Novo_CT_1h.dcm")
print(ds)
print("-"*20)
ds.PatientName = "Matheus"
ds.PatientBirthDate= "01011996"
ds.save_as("Novo_CT_1h.dcm",ds)
print(ds)