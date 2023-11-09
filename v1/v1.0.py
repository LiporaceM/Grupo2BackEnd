import pydicom
import matplotlib.pyplot as plt
import numpy as np
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