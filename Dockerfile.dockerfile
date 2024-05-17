FROM ubuntu:latest 
LABEL authors="Maansingh.Shekhawat"
#dockerENV DOCKER_OPTS="--dns 8.8.8.8"
RUN apt update
RUN apt install python3 python3-pip -y
RUN apt install python3-flask -y
WORKDIR /app

COPY app.py /app/

ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
