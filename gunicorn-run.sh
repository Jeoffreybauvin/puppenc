#!/bin/bash

gunicorn --log-level=DEBUG -w 4 -b 0.0.0.0:8000 -k gevent run:app
