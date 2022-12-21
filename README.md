# Python Docker Flask 

## Introduction
This is an example project to be used for learning port networking and application deployment in docker.

## Prerequisites
Docker
- https://www.docker.com/get-started

Git 
- https://git-scm.com/

## Architecture

The docker container that is built contains a python applications using the flask framework, this is running on a specified internal port which is mapped to an external port on the host machine. 
This means that we can have any number of applications running on the same internal port without getting port conflicts through deployment. 
The application can be interacted with via curl requests using the following format:
- curl http://localhost:{external port of container}/{app route extension in app/app.py}

## To run the container 
- Pull the code from github into a local repo
- In the project root folder (containing the dockerfile) run 'docker build -t pdf:latest .'
  - docker calls the docker command 
  - build instructs docker to build an image from a dockerfile 
  - pdf is the name of the image 
  - latest is the version tag
  - . is the path to the dockerfile which is only a . as it is in the directory
- Now we have the image built locally we can reference it in the docker-compose.yml and run it
  - Note: We can reference docker images that exist in dockerhub in a docker-compose and docker will automatically pull them down  
- Run 'docker-compose up -d'
- This deploys all the services within the docker compose to the application stack 'PDF' (python docker flask)
- Run curl http://localhost:{external port of container referenced in docker-compose} 
- default port is 5000
- This will return a html page that is stored in the templates directory  

## Tasks 
- Can you change the external port that the app listens on 
- Can you change the internal port that the app is running on 
- Can you add another app route to the application that responds to a curl request 
- Can you add a dependency to the requirements.txt that is required in the code and rebuild the docker image 
- Can you pull a branch and make a merge request into master 
- Can you change the base image in the dockerfile and rebuild the image 



