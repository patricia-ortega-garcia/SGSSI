import hashlib
import zipfile
import os

#Hash a buscar: 
hashBuscado = 'e5ed313192776744b9b93b1320b5e268'

# Nombre del archivo ZIP que contiene las imágenes
carpetaZip = 'imagen.zip'

# Abre la carpeta zip y mirar el hash de
with zipfile.ZipFile(carpetaZip, 'r') as zipf:
    for elemento in zipf.namelist():
        imagen = zipf.read(elemento)
        
        # Calcula el hash de la foto
        hashAct = hashlib.md5(imagen).hexdigest()
        
        if hashAct == hashBuscado:
        	print('Se ha encontrado la imagen buscada')
        	print(f'Archivo: {elemento}, Hash MD5: {hashAct}')
        
        

