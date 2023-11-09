import pydicom
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import filters, measure, morphology

# Carregar a Imagem
ds = pydicom.dcmread("C:/Users/202302417949/Grupo2BackEnd/Novo_CT_1h")
imagem = ds.pixel_array

# Visualizar uma parte da imagem original
plt.imshow(imagem[0], cmap='gray')
plt.title("Primeira fatia")
plt.show()

# Visualizar outra parte da imagem original
plt.imshow(imagem[imagem.shape[0] // 2], cmap='gray')
plt.title("Segunda fatia")
plt.show()

# Aplicar um filtro de média slice por slice
imagem_filtrada = np.array([cv2.blur(slice, (5, 5)) for slice in imagem])

# Visualizar uma fatia da imagem filtrada
plt.figure()
plt.imshow(imagem_filtrada[imagem_filtrada.shape[0] // 2], cmap='gray')
plt.title('Imagem Filtrada')
plt.show()

# Limiarização simples slice por slice
_, imagem_limiar = cv2.threshold(imagem_filtrada[imagem_filtrada.shape[0] // 2], 50, 255, cv2.THRESH_BINARY)

plt.figure()
plt.imshow(imagem_limiar, cmap='gray')
plt.title('Imagem Limiarizada')
plt.show()

# Dilatação slice por slice

kernel = np.ones((5, 5), np.uint8)
imagem_dilatada = np.array([cv2.dilate(slice, kernel) for slice in imagem_limiar])

plt.figure()
plt.imshow(imagem_dilatada[imagem_dilatada.shape[0] // 2], cmap='gray')
plt.title('Imagem Dilatada')
plt.show()

# Rotulagem de componentes conectados
imagem_dilatada_8bits = cv2.convertScaleAbs(imagem_dilatada)
_, labels = cv2.connectedComponents(imagem_dilatada_8bits)

plt.figure()
plt.imshow(labels, cmap='nipy_spectral')
plt.title('Imagem Rotulada')
plt.show()

## Modificando a imagem no DICOM
ds.PixelData = labels.astype(np.uint8).tobytes()

# Atualizando as tags DICOM para garantir consistência
ds.Rows, ds.Columns = labels.shape
ds.SamplesPerPixel = 1
ds.BitsStored = 8
ds.BitsAllocated = 8
ds.HighBit = 7

# Salvando como um novo arquivo DICOM
ds.save_as("C:/Users/202302417949/Grupo2BackEnd/Novo_Att_CT_1h")

# 4. Leitura do arquivo DICOM modificado
ds_modificado = pydicom.dcmread("C:/Users/202302417949/Grupo2BackEnd/Novo_Att_CT_1h")
imagem_reaberta = ds_modificado.pixel_array

# 5. Visualização da imagem reaberta
plt.figure()
plt.imshow(imagem_reaberta[0, :, :], cmap='gray')  # assumindo que 'imagem_reaberta' é uma matriz 3D
plt.title('Imagem Modificada Reaberta')
plt.show()