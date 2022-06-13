#!/bin/bash

export NODE_PATH=/home/conclave_setup/jiff/node_modules
echo $NODE_PATH
export PYTHONPATH=$PYTHONPATH:/home/conclave_setup/conclave
python --version




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


	python3 create_input.py $1 $2 $3 $4

	python protocol.py config_1.json &

	python protocol.py config_2.json &

	python -m cProfile -o $5 protocol.py config_3.json &

	myjobs=$(jobs -p)

	node server.js &

	wait $myjobs
	
	pkill -s 0


