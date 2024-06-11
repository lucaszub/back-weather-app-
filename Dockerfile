# Utilisation de l'image de base Python 3.9
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers nécessaires (le fichier de dépendances et le code source)
COPY requirements.txt .
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port sur lequel l'application FastAPI écoute
EXPOSE 8000

# Commande pour exécuter l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
