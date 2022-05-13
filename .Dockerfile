FROM python:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev

RUN pip install pygame

ENV SDL_VIDEODRIVER=dummy