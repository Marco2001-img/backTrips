# Imagen base oficial de Python
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /code

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    netcat-openbsd gcc postgresql-client libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos y requisitos
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Comando de arranque puede ir aquí o en docker-compose.yml
