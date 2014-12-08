# nat-balancer

nat-balancer is a small app for managing source routing for NAT VPNs with multiple outbound connections.

### Prerequisites

These steps were tested on Ubuntu 14.04. Your specific distribution's requirements may differ.

```sh
$ sudo apt-get install -y python-pip python-dev python-psycopg2 libpq-dev libmysqlclient-dev
$ sudo pip install -r requirements.txt
```

### Running in Development Mode

```sh
$ ./manage.py syncdb
$ ./manage.py runserver
```
