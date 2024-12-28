#! /bin/bash

# Down docker
docker-compose down

# Pull latest changes
git pull

# Up docker
./install.sh