FROM python:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev swig

RUN pip install pygame gym["all"] opencv-python twine

ENV SDL_VIDEODRIVER=dummy