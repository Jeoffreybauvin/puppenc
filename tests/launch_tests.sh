#!/bin/bash

# $1 is my api URL (http://127.0.0.1:5000)

resttest.py --url=$1  tests.yaml
