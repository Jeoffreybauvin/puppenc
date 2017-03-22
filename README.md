# puppenc

A simple external node classifier (ENC) for Puppet


### Dev environment

**docker-compose.yml**

```
version: '2'
services:
  puppenc-api:
    image: puppenc/api:latest
    restart: always
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
```

Then :

```
docker-compose up
docker-compose exec puppenc-api python shell.py
```


```
$ sudo apt-get install libmysqlclient-dev
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Tests

I'm using [pyresttest](https://github.com/svanoort/pyresttest) :

**In my  virtualenv :**

```
$ pip install pyresttest

$ cd tests

$ (venv)~/puppenc/tests(develop ✗) ./launch_tests.sh http://127.0.0.1:5000
Test Group Environments SUCCEEDED: : 5/5 Tests Passed!
Test Group Start SUCCEEDED: : 1/1 Tests Passed!
```


## Some links related to Puppet's ENC

https://docs.puppet.com/guides/external_nodes.html#enc-output-format
