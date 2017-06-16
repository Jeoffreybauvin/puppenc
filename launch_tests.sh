#!/bin/bash

docker-compose -f tests/docker-compose.yml up -d

sleep 10

# database creation
docker-compose  -f tests/docker-compose.yml exec puppenc-api-tests python shell.py --setup

# $1 is my api URL (http://127.0.0.1:5000)
if [[ $# -eq 0 ]] ; then
  url='http://127.0.0.1:5000'
else
  url=$1
fi

docker-compose  -f tests/docker-compose.yml exec puppenc-api-tests resttest.py --url=${url} tests/tests.yaml --log info
docker-compose  -f tests/docker-compose.yml down
