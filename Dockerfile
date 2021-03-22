FROM python:3.7.3-slim

WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y ffmpeg libsndfile1

# Upgrade pip
RUN pip install --upgrade pip

# Install requirements
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN rm -rf /var/lib/apt/lists/*

COPY . /app/

EXPOSE 8000