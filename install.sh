#!/bin/bash

#install npm and node for Jiff
sudo apt update
sudo apt install nodejs npm


node --version
nodejs --version

cd home/

sudo git clone https://github.com/multiparty/jiff.git

cd jiff

sudo npm install
