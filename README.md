# backend-weather-app

## Déployer son application

### Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Docker : [Instructions d'installation](https://docs.docker.com/engine/install/)
- Un compte Docker Hub : [Créer un compte](https://hub.docker.com/signup)

### Étape 1 : Build de l'image Docker

Construisez l'image Docker de votre application FastAPI avec la commande suivante :

```bash
docker build -t lucaszub/fastapiimage:v6 .
```

Pour tester l'image en local, exécutez :

```bash
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6
```

### Étape 2 : Push de l'image sur Docker Hub

Taguez l'image pour Docker Hub :

```bash
docker tag lucaszub/fastapiimage:v6 lucaszub/fastapiimage:v6
```

Puis, poussez l'image sur Docker Hub :

```bash
docker push lucaszub/fastapiimage:v6
```

### Étape 3 : Connexion SSH sous Windows

Pour vous connecter à votre serveur EC2 via SSH sous Windows, utilisez les commandes suivantes :

```powershell
icacls "cle-weather-app-project.pem" /inheritance:r /grant:r "$($env:USERNAME):(R)"
ssh -i "cle-weather-app-project.pem" ubuntu@ec2-52-47-201-9.eu-west-3.compute.amazonaws.com
```

### Étape 4 : Installer Docker sur le serveur

Suivez les instructions officielles pour installer Docker sur Ubuntu : [Installation Docker sur Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

### Étape 5 : Se connecter à Docker Hub

Connectez-vous à Docker Hub depuis votre serveur :

```bash
docker login
```

### Étape 6 : Puller l'image Docker et tester en local

Puller l'image Docker depuis Docker Hub :

```bash
sudo docker pull lucaszub/fastapiimage:v6
```

Lancez l'image pour tester en local :

```bash
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6
```

### Étape 7 : Accéder à l'application déployée

Ouvrez les règles de sécurité de votre serveur pour autoriser le trafic sur le port 8000.

Récupérez l'adresse IP publique de votre serveur et ajoutez le port à la fin de l'adresse :

```plaintext
http://<adresse_ip_publique>:8000
```

### Conclusion

Vous avez maintenant déployé votre application FastAPI sur un serveur en utilisant Docker. Pour toute question ou amélioration, n'hésitez pas à ouvrir une issue ou à proposer une pull request sur le repository.

