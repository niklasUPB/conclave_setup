#!/bin/bash

#install npm and node for Jiff
if [ $1 = "jiff_d"  ] || [ $1 = "all" ]
then
	sudo apt update
	sudo apt install nodejs npm

	node --version
	npm --version
fi


if [ $1 = "jiff" ] || [ $1 = "all" ]
then
	sudo git clone https://github.com/multiparty/jiff.git

	cd jiff

	sudo npm install
	cd ..
	
fi

if [ $1 = "conda" ] || [ $1 = "all" ]
then
	sudo apt install wget
	sudo mkdir conda_install
	cd conda_install
	sudo wget https://repo.continuum.io/archive/Anaconda3-2022.05-Linux-x86_64.sh
	sudo bash Anaconda3-2022.05-Linux-x86_64.sh
	#conda create --name 3.5 python=3.5.6
	#conda activate 3.5
	cd ..
fi

if [ $1 = "cmake" ] || [ $1 = "all" ]
then
	cd cmake_install
	sudo tar -xvf cmake-3.23.2.tar.gz
	sudo make
	sudo make install
	cd ..

fi

if [ $1 = "conclave" ] || [ $1 = "all" ]
then
	#conda activate 3.5
	sudo git clone https://github.com/multiparty/conclave.git
	cd conclave
	pip install -r requirements.txt
	python3 setup.py build
	python3 setup.py install
	cd .. 
	
fi








