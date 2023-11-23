import pydicom
import matplotlib.pyplot as plt
import numpy as np


ds = pydicom.dcmread("C:/Users/Matheus/Desktop/ibmec/Grupo2BackEnd/Novo_CT_1h.dcm", force=True)


if 'PixelData' in ds:
    pixel_data = ds.PixelData

    rows = ds.Rows
    columns = ds.Columns


    dtype = np.int16 if ds.BitsAllocated == 16 else np.uint8


    imagem = np.frombuffer(pixel_data, dtype=dtype).reshape((rows, columns))

    plt.imshow(imagem, cmap='gray')
    plt.title("Imagem Original")
    plt.show()

 
    plt.imshow(imagem[imagem.shape[0] // 2], cmap='gray')
    plt.title("Segunda fatia")
    plt.show()
else:
    print("PixelData attribute not found in the DICOM file.")
