#! /bin/bash

clear

sudo apt-get update
sudo apt-get install -y python3 python3-pip

pip3 ./setting/setting_env.py

clear

docker compose up --build -d