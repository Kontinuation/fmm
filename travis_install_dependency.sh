#!/bin/bash

if [ $TRAVIS_OS_NAME = 'osx' ]; then
  brew update;
  brew install boost gdal libomp swig || true;
else
  sudo add-apt-repository -y ppa:ubuntugis/ppa;
  sudo apt-get -q update;
  sudo apt-get -y install libboost-dev libboost-serialization-dev gdal-bin libgdal-dev make cmake;
  sudo apt-get -y install swig python3-dev python3-pip;
fi
python3 -m pip install --upgrade pip setuptools wheel
