import pydicom
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the DICOM file
dicom_file_path = "C:/Users/Matheus/Desktop/ibmec/Grupo2BackEnd/Novo_CT_1h.dcm"
ds = pydicom.dcmread(dicom_file_path, force=True)

# Check if 'PixelData' is present in the DICOM file
if 'PixelData' in ds:
    # Extract pixel data and image dimensions
    pixel_data = ds.PixelData
    rows = ds.Rows
    columns = ds.Columns

    # Convert pixel data to NumPy array
    dtype = np.int16 if ds.BitsAllocated == 16 else np.uint8
    imagem = np.frombuffer(pixel_data, dtype=dtype).reshape((rows, columns))

    # Display the original DICOM image
    plt.imshow(imagem, cmap='gray')
    plt.title("Imagem Original")
    plt.show()

    # Normalize pixel values to the range [0, 255]
    normalized_imagem = ((imagem - np.min(imagem)) / (np.max(imagem) - np.min(imagem)) * 255).astype(np.uint8)

    # Apply a mean filter to the image
    filtered_image = cv2.blur(normalized_imagem, (5, 5))

    # Display the filtered image
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Imagem Filtrada')
    plt.show()

    # Apply a Gaussian filter to the image
    blurred_image = cv2.GaussianBlur(normalized_imagem, (5, 5), 0)

    # Display the Gaussian filtered image
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Filtro Gaussian')
    plt.show()

    # Apply a median filter to the image
    median_blurred_image = cv2.medianBlur(normalized_imagem, 5)

    # Display the median filtered image
    plt.imshow(median_blurred_image, cmap='gray')
    plt.title('Filtro Median')
    plt.show()

else:
    print("PixelData attribute not found in the DICOM file.")
