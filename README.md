# puppenc
A simple external node classifier (ENC) for Puppet

# Dev environment

docker-compose.yml

~~~
version: '2'
services:
  puppenc-api:
    image: puppenc/api:latest
    ports:
      - "5000:5000"
    volumes:
      -  /root/puppenc/api:/puppenc
    links:
      - puppenc-mysql
    entrypoint:
      - python
      - run.py
  puppenc-mysql:
    image: mysql:5.6
    ports:
      - "3306"
    environment:
      MYSQL_ROOT_PASSWORD: 'puppenc'
      MYSQL_DATABASE: 'puppenc'
~~~

Après :

~~~
docker-compose up
docker-compose exec puppenc-api python shell.py
~~~

~~~
$ sudo apt-get install libmysqlclient-dev
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements.txt
~~~

# Stuff to know about Puppet's ENC

https://docs.puppet.com/guides/external_nodes.html#enc-output-format
