# puppenc
A simple external node classifier (ENC) for Puppet

# Dev environment

~~~
docker pull mysql:5.6
docker run --name mysql-puppenc -e MYSQL_ROOT_PASSWORD=puppenc -e MYSQL_DATABASE=puppenc -d mysql:5.6
~~~


~~~
$ sudo apt-get install libmysqlclient-dev
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements.txt
~~~

# Stuff to know about Puppet's ENC

https://docs.puppet.com/guides/external_nodes.html#enc-output-format
