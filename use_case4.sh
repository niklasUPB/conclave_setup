#!/bin/bash

export NODE_PATH=/home/conclave_setup/jiff/node_modules
echo $NODE_PATH
export PYTHONPATH=$PYTHONPATH:/home/conclave_setup/conclave
export NODE_OPTIONS=--max_old_space_size=128000
sysctl -w vm.max_map_count=65530000



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
		


	python3 create_input_use_case4.py $2  $3 


fi


if [ $1 = "server" ]
then
	time --output=./Results/use_case4_local -a -v node server.js
fi
if [ $1 = "eins" ]
then
	time --output=./Results/use_case4_local -a -v python protocol_use_case4.py config_1_use_case4.json
fi	
if [ $1 = "zwei" ]
then
	time --output=./Results/use_case4_local -a -v python protocol_use_case4.py config_2_use_case4.json
fi	
