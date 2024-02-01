# base image
FROM python:3.10.12
# setup environment variable
ENV PYTHONUNBUFFERED 1

# create root directory
RUN mkdir /demo

# set work directory
WORKDIR /demo

# copy current directory contents to container
ADD . /demo/

# run this command to install all dependencies
RUN pip install -r requirements.txt
