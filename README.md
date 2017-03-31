# puppenc

A simple external node classifier (ENC) for Puppet

### Specs

| Object | Methods | Description |
| --- | --- | --- |
| Classes | `GET`, `POST`, `DELETE`  | Manage Puppet's classes
| Environments | `GET`, `POST`, `DELETE`  | Manage Puppet's environments
| Hostgroups | `GET`, `POST`, `DELETE`  | Manage Puppet's hostgroups
| Nodes | `GET`, `POST`, `PUT`, `DELETE`  | Manage Puppet's nodes
| ENC | `GET` | Manage ENC resources

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
      - "5001:5001"
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

### I need a GUI

You should not need a GUI. But, if you want to, you can use (Flask_Admin)[https://flask-admin.readthedocs.io/en/latest/].

**In my virtualenv :**

```
$ docker-compose exec puppenc-api python admin.py
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 730-803-037
```

And browse to (http://127.0.0.1:5001/admin/)[http://127.0.0.1:5001/admin/]

## Some links related to Puppet's ENC

https://docs.puppet.com/guides/external_nodes.html#enc-output-format
