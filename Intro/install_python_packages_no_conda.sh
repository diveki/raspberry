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

# IR
sudo apt-get install --yes python3-pyqt5
sudo apt-get install --yes python3-pyqt5.qtsvg
sudo apt-get install --yes python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns


# Sound

pip install pyaudio
pip install SpeechRecognition
