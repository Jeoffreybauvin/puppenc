#!/bin/bash

# $1 is my api URL (http://127.0.0.1:5000)

if [[ $# -eq 0 ]] ; then
  url='http://127.0.0.1:5000'
else
  url=$1
fi


resttest.py --url=$url tests.yaml
