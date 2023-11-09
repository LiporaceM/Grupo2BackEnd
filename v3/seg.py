import os
import pydicom
import nibabel as nib
import numpy as np
from totalsegmentator.python_api import totalsegmentator

# Função para tentar ler um arquivo DICOM
def try_read_dicom(file_path):
    try:
        return pydicom.dcmread(file_path)
    except pydicom.errors.InvalidDicomError:
        return None

def dicom_to_nifti(dicom_folder, output_filename):
    # Tente ler os arquivos DICOM e colete apenas os válidos
    dicom_files = [f for f in (try_read_dicom(os.path.join(dicom_folder, file)) for file in os.listdir(dicom_folder) if os.path.isfile(os.path.join(dicom_folder, file))) if f is not None]
    
    # Ordenar os arquivos DICOM pelo número da imagem
    dicom_files.sort(key=lambda x: int(x.InstanceNumber) if x.InstanceNumber is not None else 0)
    
    # Criar um array 3D com os dados DICOM
    dicom_data = np.stack([s.pixel_array for s in dicom_files])
    
    # Criar uma imagem NIFTI
    nifti_image = nib.Nifti1Image(dicom_data, np.eye(4))
    
    # Salvar a imagem NIFTI
    nib.save(nifti_image, output_filename)

def main():
    # Diretório das imagens DICOM
    input_path = "C:/Users/202302417949/Grupo2BackEnd/Novo_CT_1h.dcm"

    if not os.listdir(input_path):
        print("O diretório não contém imagens DICOM.")
        return

    # Convertendo DICOM para NIFTI
    nifti_filename = os.path.join(input_path, "output.nii")
    dicom_to_nifti(input_path, nifti_filename)

    # Diretório de saída para segmentações
    output_path = os.path.join(input_path, "segmentations")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Segmentação usando TotalSegmentator
    totalsegmentator(nifti_filename, output_path)

    print(f"Segmentações salvas em: {output_path}")

if __name__=='__main__':
    main()