import requests
import pydicom
from flask import Flask, request, send_file, Response


url = "http://127.0.0.1:5000//anonimizar"
file_path = "C:/Users/202302417949/Grupo2BackEnd/Novo_CT_1h.dcm"
output_path = "arquivo_anonimizado.dcm"

with open(file_path, 'rb') as file:
    response = requests.post(url, files={"file": file})

    if response.status_code == 200:
        with open(output_path, 'wb') as output_file:
            output_file.write(response.content)
        print(f"Arquivo anonimizado salvo como {output_path}")
    else:
        print(f"Erro: {response.status_code} - {response.text}")
