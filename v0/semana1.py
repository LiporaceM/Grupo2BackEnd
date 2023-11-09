import pydicom
ds = pydicom.dcmread("C:/Users/202302417949/Grupo2BackEnd/Novo_CT_1h")
ds.PatientName = "Matheus"
ds.PatientBirthDate= "01011996"
ds.save_as("NovoCT_1h.dcm",ds)
print("'"*20)