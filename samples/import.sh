#!/bin/bash

# $1 type (hostgroups, environments, ...)

url="http://127.0.0.1:5000/api/v1"

case "$1" in
"environments")
    for i in `cat environments.json`; do
       curl -H "Content-Type: application/json" -X POST ${url}/environments -d $i
    done
    ;;
"3")
    echo "caca"
    ;;
*)
    echo "Nothing to do"
    exit
    ;;
esac
