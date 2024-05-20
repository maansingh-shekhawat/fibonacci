<h1 align="center">Fibonacci Sequence Flask API

## Overview
This project consists of a Flask API that calculates the nth Fibonacci number. It includes Docker and Kubernetes configurations for deployment.

	##Files
- Dockerfile: Contains the instructions to build the Docker image for the Flask API.
- app.py: The Flask application that defines the Fibonacci API.
- app.yaml: Kubernetes deployment and Ingress configuration for the Flask API.

## Dockerfile

# Description
This Dockerfile creates an image based on Ubuntu, installs Python, Flask, and sets up the working directory. It then copies the app.py file into the container and configures the entry point to run the Flask app.


### Build Docker Image
To build the Docker image, run:

docker build -t dockerfile


### Run Docker Container
To run the Docker container, execute:

docker run -p 5000:5000 fibotest:latest

push the docker image to docker hub 
Tag Your Local Image:

docker image tag local-image:tag username/repository:tag

example docker images tag 05479671be62:tag maan25/fib:tag


## app.py

### Description
The app.py file contains the This code sets up a simple Flask web application that calculates Fibonacci numbers based on user input. 
 #Dependencies:
Flask: A micro web framework for Python.
jsonify: A Flask function to convert Python dictionaries to JSON responses.
request: A Flask object to handle HTTP requests.


##Fibonacci Sequence function:
The fibonacci(n) function calculates the nth Fibonacci number.
If n is less than or equal to 0, it returns a message indicating that the input should be a positive integer.
The function retrieves the value of the query parameter n (defaulting to 1 if not provided).

##Logging is enabled using below

file_handler: Logs messages to a file named “app.log”.

stream_handler: Logs messages to the console (standard output).

this creates app.log file which generates  the logs 
as Generated Fibonacci number for n=%s, result=%s'
we can use fluntd  data collector which can ship these logs to prometheus and grafana

## Running Locally
To run the Flask application locally:

python3 app.py

Then navigate to http://127.0.0.1:5000/fibonacci?n=10 to get the 10th Fibonacci number.

## deployment.yaml

### Description
The app.yaml file contains Kubernetes configurations for deploying the Flask API. It includes a Deployment with two replicas and an Ingress for external access.
 
To apply this Kubernetes configuration to your cluster, follow these steps:
1.	Create or Update the Deployment and Ingress 
	Save the provided YAML configuration to a file Here its ( app.yaml).
	Open a terminal and navigate to the directory containing the file.
	Run the following command to create or update the deployment:
	kubectl apply -f app.yaml.yaml
	This will create two replicas of the fibonacci application.
	This will configure routing rules and TLS termination for the specified hostname.
2.	Verify Deployment and Ingress:
	Check the status of the deployment:
	kubectl get deployments
	Verify that the fibonacci-deployment has the desired number of replicas.
	Check the status of the ingress:
	kubectl get ingress
	Ensure that the ingress is created and routes traffic correctly.
3.	DNS Configuration:
	Make sure that the hostname (fibonacci.platdev2-cust-eastus.bentleyhosted.com) resolves to the IP address of your cluster.
4.	TLS Certificate:
	Verify that the TLS certificate is correctly associated with the ingress.
5.	Access the Application:
	Open a web browser and navigate to https://fibonacci.platdev2-cust-eastus.bentleyhosted.com/fibonacci?n=10
	You should see your Fibonacci application running!
 

Setting up a CI/CD pipeline with Kubernetes involves automating the build, test, and deployment processes for your applications running on Kubernetes clusters. 

1. Kubernetes Cluster Preparation:
Ensure you have a Kubernetes cluster ready. You can use tools like Minikube for local development or a managed Kubernetes service like Azure Kubernetes Service (AKS) for production.
Set up kubectl to interact with your cluster.
2. Application Containerization:
Create a Dockerfile for each microservice in your application. Specify the containerization blueprint, including dependencies, environment variables, and entry points.
Build Docker images for services 
3. Kubernetes Deployment and Service Creation:
Define Kubernetes Deployment configurations for each microservice. Specify the desired replicas, image references, and resource limits.
Create Services to expose your microservices within the cluster. Use LoadBalancer, NodePort, or Ingress based on your requirements.
4.CI/CD Pipeline with Jenkins (or Alternatives):
Set up Jenkins (or any other CI/CD tool of your choice) within your Kubernetes cluster.
Configure a Jenkins pipeline that:Pulls your code from a Git repository (e.g., GitHub).
Builds the Docker images using the Dockerfile.
Pushes the images to a container registry (e.g., Docker Hub, Azure Container Registry).
Deploys the updated images to your Kubernetes cluster.



**Implement monitoring and logging solutions:**
We can use  tools like Prometheus, Grafana to  monitor resource utilization, response times, and error rates.
Set up alerts for critical events.


**Consider implementing rollbacks:**
If a deployment fails or causes issues, roll back to the previous version using Kubernetes Rolling Updates or Blue-Green Deployments.


## Summary
This project demonstrates deploying a simple Fibonacci calculator API using Flask, Docker, and Kubernetes. Follow the steps above to build, run, and deploy the application.


