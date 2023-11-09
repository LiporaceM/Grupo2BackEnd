from flask import Flask, request, send_file
from flask import Flask, jsonify
import pydicom
import io

app = Flask(__name__)

@app.route('/anonimizar', methods=['POST'])
def anonimizar():
    # Verificar se o arquivo foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Arquivo não enviado."}), 400

    file = request.files['file']
    dicom_data = io.BytesIO(file.read())
    dataset = pydicom.dcmread(dicom_data)

    # Anonimizar metadados
    tags_to_remove = ['PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex']
    for tag in tags_to_remove:
        if tag in dataset:
            delattr(dataset, tag)

    # Salvar o arquivo DICOM anonimizado em um buffer
    output_buffer = io.BytesIO()
    dataset.save_as(output_buffer)

    # Retornar o arquivo anonimizado
    output_buffer.seek(0)
    return send_file(output_buffer, as_attachment=True, download_name="anonimizado.dcm", mimetype="application/dicom")

if __name__ == '__main__':
    app.run(debug=True)

