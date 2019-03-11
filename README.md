# statsmodels_json

# Introduction

Statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. The package is released under the open source Modified BSD (3-clause) license. The online documentation is hosted at statsmodels.org.

For many reasons,my enterprise applications maybe devedeveloped by php, java, etc.,it is not convenient to use statsmodels, so I create a json interface in web json fro statsmodels,which is convenient using in my enterprise applications. 

It is only necessary to submit the parameter data according to the interface parameters corresponding to different statistical models, and the various results of the statsmodels model can be returned by json.The statemodels results in json can be obtained by submitting parameters according to the interface parameters of the statesmodels.

# Dependency(My development environment)
## CentOS7.5
## python 3.6(using conda install)

Flask                    0.12.2
mod-wsgi                 4.5.24+ap24vc14
numpy                    1.13.1
pandas                   0.20.3
scipy                    1.1.0
statsmodels              0.8.0


# Installation
## Create python environment and entrance
$ virtualenv py36 --python=python3
$ source py36/bin/activate

## Install packages

pip install flask numpy pandas statsmodels scipy uwsgi

## Modify files for the correct path and ip address
uwsgi.ini
wsgi.py


# Using
In you environment(python3.6)

In devedeveloped environment
$ python manage.py

or in product environment

$ uwsgi --ini uwsgi.ini
