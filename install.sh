#! /bin/bash

clear

sudo apt-get update
sudo apt-get install -y python3

python3 ./setting/setting_env.py

clear

sudo docker-compose up --build -d
