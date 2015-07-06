
# Tech Arch Design

## Backend
Restful API for backend.

JSON + vnd.xyz for data trasmission.

Python2.7 + flask as application main framework.

* flask-restful for restful service
* flask-sqlalchemy for database mgmt
* flask-marshmallow for serialization
* flask-scripts for auto mgmt tool scripts
* flask-migrate for database version migrations
* ...


Integration with 3rd Services, LBS, Paycheck, SNS, OAuth2...

## Frontend

HTML5 for base.

Angular, bootstrap and its extensions for framework.

Cordova as framework for iOS and Android.

## Conf


### Python

* pyenv with virtualenv as python version mgmt, use 'store' as local env.
* tox for building, integrates the following.
* nosetests, coverage-all for unittest.
* flake8, pep8, autopep8 for code style.
* distutil2 for setup and distributions.
* pip and requestments for dependency mgmt.

### HTML5

* grunt, gulp for building.
* bower for css/js/html dependency mgmt.
* npm for nodejs dependency mgmt.

### Docs

* markdown for doc writting.
* gitchangelog for changelog gen.

## 3rd Service for Conf

Travis for CI, alternative: CircleCI.
