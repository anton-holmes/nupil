FROM ubuntu:24.04

RUN apt-get update -y
RUN apt-get install -y python3.12
# Установить
# && apt-get install man-db -y unminimize

RUN ln -s /usr/bin/python3.12 /usr/bin/python
# RUN pip3 --version && sleep 5 -minimal python3-pip

WORKDIR /nupil_mount
RUN mkdir /nupil_mount/nupil

COPY main.py /nupil_mount/nupil

# CMD ["python", './nupil/main.py']

# && apt upgrade -y 
