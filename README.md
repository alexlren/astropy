# astropy

Implementation of a simple blockchain in python
It can serve as a POC or to test advanced features of my estel project

## Install as a user

```
pip install --user astropy
```

## Development

### Install dependencies

```
$ pip install --user -r requirements.txt
$ pip install --user -r requirements-dev.txt
```

### Documentation

```
$ python setup.py build_sphinx
```

### Run tests

#### Run all tests (including flake8 and mypy)

```
$ tox
```

#### Run flake8

```
$ tox -e flake8
```

#### Run mypy

```
$ tox -e mypy
```
