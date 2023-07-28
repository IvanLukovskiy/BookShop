FROM python:3.11

#SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

# port
EXPOSE 8000

# copy app files
COPY . /app
