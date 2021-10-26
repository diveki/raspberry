#!/bin/bash

conda install --yes ipython
conda install --yes numpy
conda install --yes matplotlib
conda install --yes -c anaconda flask
conda install --yes -c anaconda unidecode

sudo apt install python3-gpiozero
pip install RPi.GPIO
pip install gpiozero
sudo pip install tweepy
sudo pip install cloud4rpi

##### Thermisztorok
pip install spidev
pip install adafruit-blinka
pip install adafruit-circuitpython-dht
sudo apt-get install --yes libgpiod2

# installing pygame
sudo apt install --yes libsdl1.2-dev
sudo apt-get install --yes build-essential libfreeimage-dev libopenal-dev libpango1.0-dev libsndfile-dev libudev-dev libasound2-dev libjpeg9-dev
sudo apt-get install --yes libtiff5-dev libwebp-dev automake
sudo apt-get install --yes python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev   libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
pip install pygame==1.9.4
