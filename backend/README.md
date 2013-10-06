## server component

The backend server is written in Python using the Flask web framework.

### Requirements

For a fresh Ubuntu 12.04 install, you need the followings:

```
sudo apt-get install build-essential python-virtualenv python-dev mongodb-server
```

You should also install ``git`` and ``vim`` (or your favorite editor).

### Set up a running instance

Here are the steps to set up a running instance

```
virtualenv env
source env/bin/activate
git clone https://github.com/yeukhon/laughing-happiness
cd laughing-happiness/backend
python setup.py develop
python __init__.py
```

If you do ``pip install nose`` to run tests, you can do this:

```
nosetests -s -v
```

