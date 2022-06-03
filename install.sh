#!/bin/bash

#install npm and node for Jiff
if [ $1 = "jiff_d" || $1 = "all" ]
then
	sudo apt update
	sudo apt install nodejs npm

	node --version
	nodejs --version
fi




if [ $1 = "jiff" || $1 = all ]
then
	cd ..

	sudo git clone https://github.com/multiparty/jiff.git

	cd jiff

	sudo npm install
	cd ..
	cd conclave_setup
fi

if [ $1 = "conda" || $1 = "all" ]
then
	sudo apt install wget
	cd conda_install
	bash Anaconda-latest-Linux-x86_64.sh
	cd ..
fi

if [ $1 = "cmake" || $1 = "all" ]
then
	cd cmake_install
	sudo tar -xvf cmake-3.23.2.tar.gz
	sudo make
	sudo make install
	cd ..
	

fi

if [ $1 = "conclave" || $1 = "all" ]
then
	pip install -r requirements.txt


fi







