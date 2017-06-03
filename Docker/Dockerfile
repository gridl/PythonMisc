# Set the base image to Ubuntu
#FROM python:3.4
FROM ubuntu
# File Author / Maintainer
MAINTAINER Vish



# Installs
RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install python3
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 5000
#CMD ["python", "app.py"]

# docker build -t vishwanath79/hellodocker .

#  docker run -p 5000:5000 vishwanath79/hellodocker

# docker commit 6ff641e387d3 vishwanath79/hellodocker
