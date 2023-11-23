import pydicom
import matplotlib.pyplot as plt
import numpy as np

# Carregar a Imagem
ds = pydicom.dcmread("C:/Users/Matheus/Desktop/ibmec/Grupo2BackEnd/Novo_CT_1h.dcm", force=True)

# Check if 'PixelData' is present in the DICOM file
if 'PixelData' in ds:
    pixel_data = ds.PixelData
    # Get image dimensions from DICOM metadata
    rows = ds.Rows
    columns = ds.Columns

    # Determine the datatype based on the BitsAllocated attribute
    dtype = np.int16 if ds.BitsAllocated == 16 else np.uint8

    # Convert the pixel data to a NumPy array
    imagem = np.frombuffer(pixel_data, dtype=dtype).reshape((rows, columns))
    
    # Visualizar a imagem original
    plt.imshow(imagem, cmap='gray')
    plt.title("Imagem Original")
    plt.show()

    # Visualizar outra parte da imagem original
    plt.imshow(imagem[imagem.shape[0] // 2], cmap='gray')
    plt.title("Segunda fatia")
    plt.show()
else:
    print("PixelData attribute not found in the DICOM file.")
