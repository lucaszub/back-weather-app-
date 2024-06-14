# backend-weather-app

# pour se connecte en ssh sous windows 
icacls "cle-weather-app-project.pem" /inheritance:r /grant:r "$($env:USERNAME):(R)"

ssh -i "cle-weather-app-project.pem" ubuntu@ec2-52-47-201-9.eu-west-3.compute.amazonaws.com



ssh -i "cle-weather-app-project.pem" ubuntu@ec2-13-38-130-150.eu-west-3.compute.amazonaws.com
deuxieme instance
# à executer sur son repertoire local  
- scp -i "C:\wild code school\weather_app\backend weather app\cle-weather-app-project.pem" -r "C:\wild code school\weather_app\backend weather app\app" ubuntu@172.31.1.233:/home/ubuntu
        # ici mettre l'ip public de l'ec2

13.38.130.150


# dans ssh
# installer docker 
https://docs.docker.com/engine/install/ubuntu/


sudo usermod -aG docker $USER

# build l'image de fast api 
sudo docker build -t python39-fastapi-app .


sudo docker run -d -p 8000:8000 python39-fastapi-app


# pour avoir l'adress ip publique
curl http://checkip.amazonaws.com




http://52.47.201.9:8000
52.47.201.9

http://52.47.201.9:8000

35.180.250.227


http://35.180.250.227:8000





# Lancement de l'application 
uvicorn main:app --reload



docker build -t fastapiimage .

docker login

docker image tag fastapiimage:latest lucaszub/fastapiimage:latest

docker push lucaszub/fastapiimage:latest
 

ssh -i "cle-weather-app-project.pem" ubuntu@ec2-35-180-37-141.eu-west-3.compute.amazonaws.com

# installer docker


docker build -t lucaszub/fastapiimage:v6 .


docker run -d -p 8000:8000 lucaszub/fastapiimage:v6


docker login

docker tag lucaszub/fastapiimage:v6 lucaszub/fastapiimage:v6
docker push lucaszub/fastapiimage:v6

sudo docker pull lucaszub/fastapiimage:v6
http://172.31.13.119:8000
172.31.13.119
172.31.13.119
http://172.31.22.136:8000

docker run -d -p 8000:8000 lucaszub/fastapiimage:v5
http://localhost:8000
http://172.31.1.233:8000
172.31.2.33
172.31.2.33
172.31.1.233


 uvicorn main:app --reload     
