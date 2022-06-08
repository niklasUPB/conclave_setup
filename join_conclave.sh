#!/bin/bash

export NODE_PATH=/home/conclave_setup/jiff/node_modules
echo $NODE_PATH
export PYTHONPATH=$PYTHONPATH:/home/conclave_setup/conclave
python --version


if [ $1 = "2222" ]
then
	if [ -d "./data" ]
	then
		rm -r data
		mkdir data	
	fi
	if [ -d "./data2" ]
	then
		rm -r data
		mkdir data2
	fi
		
	if [ -d "./data3" ]
	then
		rm -r data
		mkdir data3
	fi

	mkdir data
	mkdir data2
	mkdir data3


fi


if [ $1 = "server" ]
then
	node server.js
fi
if [ $1 = "eins" ]
then
	python protocol.py config_1.json
fi	
if [ $1 = "zwei" ]
then
	python protocol.py config_2.json
fi	
if [ $1 = "drei" ]
then
	python protocol.py config_3.json
fi
