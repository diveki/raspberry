#!/bin/bash

pip install --upgrade pip
pip install ipython
echo "export PATH=/home/pi/.local/bin:$PATH" >> /home/pi/.bashrc
source ~/.bashrc

pip install numpy
pip install --upgrade numpy
pip install matplotlib
pip install Flask
pip install Unidecode

sudo apt install python3-gpiozero
pip install RPi.GPIO
pip install gpiozero
sudo pip install tweepy
sudo pip install cloud4rpi

# scipyhoz szukseges csomagok
sudo apt-get install --yes libatlas-base-dev gfortran
pip install scipy


##### Thermisztorok
pip install spidev
pip install adafruit-blinka
pip install adafruit-circuitpython-dht
sudo apt-get install --yes libgpiod2

# installing pygame
#sudo apt install --yes libsdl1.2-dev
#sudo apt-get install --yes build-essential libfreeimage-dev libopenal-dev libpango1.0-dev libsndfile-dev libudev-dev libasound2-dev libjpeg9-dev
#sudo apt-get install --yes libtiff5-dev libwebp-dev automake
#sudo apt-get install --yes python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev   libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
#pip install pygame==1.9.4

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install --yes cmake gfortran
sudo apt-get install --yes python3-dev python3-numpy
sudo apt-get install --yes libjpeg-dev libtiff-dev libgif-dev
sudo apt-get install --yes libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install --yes libgtk2.0-dev libcanberra-gtk*
sudo apt-get install --yes libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install --yes libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev
sudo apt-get install --yes libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install --yes libjasper-dev liblapack-dev libhdf5-dev
sudo apt-get install --yes protobuf-compiler

pip install opencv-contrib-python
