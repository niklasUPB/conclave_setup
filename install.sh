#!/bin/bash

#install npm and node for Jiff
if[$1 = jiff_d || $1 = all]
then
	sudo apt update
	sudo apt install nodejs npm
fi

node --version
nodejs --version


if [$1 = jiff || $1 = all]
then
	cd ..

	sudo git clone https://github.com/multiparty/jiff.git

	cd jiff

	sudo npm install
	cd ..
	cd conclave_setup
fi

if[$1 = conda|| $1 = all]
then
	sudo apt install wget
	bash Anaconda-latest-Linux-x86_64.sh

fi





