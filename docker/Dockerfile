FROM python:3.11-slim-bullseye

WORKDIR /usr/src

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential gcc libsndfile1 libgl1-mesa-glx ffmpeg libsm6 libxext6 \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /usr/src/app