# Usar una imagen base de Ubuntu
FROM ubuntu:latest

# Actualizar el sistema e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Copiar el archivo main.py al contenedor
COPY main.py /app/main.py

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Instalar las dependencias de Python (si las tienes en un archivo requirements.txt)
# COPY requirements.txt /app/requirements.txt
# RUN pip3 install -r requirements.txt

# Comando para ejecutar el script Python
CMD ["python3", "main.py"]
