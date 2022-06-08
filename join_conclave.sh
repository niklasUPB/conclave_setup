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
		
	if [ -d "./data" ]
	then
		rm -r data
		mkdir data2
	fi

	mkdir data
	mkdir data2
	mkdir data3


fi


if [ $1 = "server" ]
then
	node server.js
fi
if [ $1 = "1" ]
then
	python protocol.py config_one.json	
fi	
if [ $1 = "2" ]
then

fi	
if [ $1 = "2" ]
then
	
fi
