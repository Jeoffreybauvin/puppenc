#!/bin/bash

gunicorn --log-level=DEBUG -w 2 -b 0.0.0.0:8000 run:app
