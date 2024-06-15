# backend-weather-app

## Déployer son application

### Build son image

```bash
docker build -t lucaszub/fastapiimage:v6 .
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6 # pour tester en local
```

### Push sur Docker Hub

```bash
docker tag lucaszub/fastapiimage:v6 lucaszub/fastapiimage:v6
docker push lucaszub/fastapiimage:v6
```

### Pour se connecter en SSH sous Windows

```powershell
icacls "cle-weather-app-project.pem" /inheritance:r /grant:r "$($env:USERNAME):(R)"
ssh -i "cle-weather-app-project.pem" ubuntu@ec2-52-47-201-9.eu-west-3.compute.amazonaws.com
```

### Installer Docker

Suivez les instructions sur [la documentation officielle de Docker](https://docs.docker.com/engine/install/ubuntu/).

### Se connecter à Docker

```bash
docker login
```

### Puller l'image Docker et tester en local

```bash
sudo docker pull lucaszub/fastapiimage:v6
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6 # pour tester en local
```

## Pour aller voir son application déployée

Ouvrir les règles de sécurité pour accéder au port 8000.

Récupérer son IP publique et ajouter le port à la fin de l'adresse :

```plaintext
http://<adresse_ip_publique>:8000
```
