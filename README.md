# Food Oasis LA

[![CI Status](https://api.travis-ci.org/foodoasisla/backend.svg?branch=master)](https://travis-ci.org/foodoasisla)



This is the repo for the backend of [Food Oasis LA](https://foodoasisla.github.io/).

## Technology Stack
  - Language: Python 3.5
  - Datastore: Postgres
  - Framework: [Django-Rest](http://www.django-rest-framework.org/)
  - [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
  - Deployment: Heroku

## Setup

**Quickstart**

1. Install Postgres and start server.
2. Clone app `git clone https://github.com/foodoasisla/backend.git`
3. Make a virtualenv (python 3) `mkvirtualenv --python=$(which python3) foodoasis`
4. Run the setup script: `make setup`

Detailed instructions are available in CONTRIBUTING.md

## Architecture Notes
The backend will serve a REST API that will initially consist of types and locations of fresh food within Los Angeles.

The current .CSV datasets have been organized into the following general categories:
Community Gardens, Farmer's Markets, Food Banks, Grocery Stores, Supermarkets & Convenience Stores.

## Tutorials
  - [Django-Rest Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/)
  - [Django-Rest 7 Part Tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/)
  - [Intro to VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
  - Suggested helper for VirtualEnv: [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io)

