#!/bin/bash

curl -X POST -H "Content-Type: application/json" \
-d '{ "name": "my_new_hostgroup" }' \
http://127.0.0.1:5000/api/v1/hostgroups



curl -X POST -H "Content-Type: application/json" \
-d '{ "name": "master" }' \
http://127.0.0.1:5000/api/v1/environments


curl -X POST -H "Content-Type: application/json" \
-d '{ "name": "role::my_class" }' \
http://127.0.0.1:5000/api/v1/classes

curl -X PUT -H "Content-Type: application/json" \
-d '{ "class_id": 1 }' \
http://127.0.0.1:5000/api/v1/hostgroups/1

curl -X POST -H "Content-Type: application/json" \
-d '{ "name": "my_server", "environment_id":1, "hostgroup_id": 1 }' http://127.0.0.1:5000/api/v1/nodes


curl -X POST -H "Content-Type: application/json" \
-d '{ "name": "my_variable", "content": "my_content" }' \
http://127.0.0.1:5000/api/v1/variables


