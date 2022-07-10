#!/bin/bash

export NODE_PATH=/home/conclave_setup/jiff/node_modules
echo $NODE_PATH
export PYTHONPATH=$PYTHONPATH:/home/conclave_setup/conclave
export NODE_OPTIONS=--max_old_space_size=16000
python --version


if [ $1 = "server" ]
then
	if [ -d "./data" ]
	then
		rm -r data
		mkdir data	
	fi
	if [ -d "./data2" ]
	then
		rm -r data2
		mkdir data2
	fi
		
	if [ -d "./data3" ]
	then
		rm -r data3
		mkdir data3
	fi


	python3 create_input.py $2 $3 $4 $5


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
	python -m cProfile -o $2 protocol.py config_3.json
fi
