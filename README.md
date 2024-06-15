# backend-weather-app


# Deployer son application 

- build son image
'''
docker build -t lucaszub/fastapiimage:v6 .

'''
'''
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6 # pour tester en local
'''
- Push sur docker hub 
'''
docker tag lucaszub/fastapiimage:v6 lucaszub/fastapiimage:v6
'''
'''
docker push lucaszub/fastapiimage:v6
'''

## # pour se connecte en ssh sous windows 
'''
icacls "cle-weather-app-project.pem" /inheritance:r /grant:r "$($env:USERNAME):(R)"
'''

'''
ssh -i "cle-weather-app-project.pem" ubuntu@ec2-52-47-201-9.eu-west-3.compute.amazonaws.com
'''

# installer docker 
https://docs.docker.com/engine/install/ubuntu/
'''
docker login
'''

'''
sudo docker pull lucaszub/fastapiimage:v6

'''
docker run -d -p 8000:8000 lucaszub/fastapiimage:v6 # pour tester en local
'''

Pour aller voir son application deployer

- ouvrir les sécurité pour aller voir 8000
- Récupéré son ip publique et rajouter le port à la fin

'''
http://<adress_ip_publique>:8000
'''





