#!/bin/bash

# run the whole code with source ./install.sh

cd ~
cd Downloads
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh

# miniconda location: /home/pi/miniconda3
# prepend path in bashrc -> yes

echo "export PATH=/home/pi/miniconda3/bin:$PATH" >> /home/pi/.bashrc

conda config --add channels rpi
sudo chown -R pi /home/pi/miniconda3/
conda install python=3.6

sudo ln -s /home/pi/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh