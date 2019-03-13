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
```
[uwsgi]
socket=0.0.0.0:5001
http=0.0.0.0:5000
chdir=/home/lbw/apis
wsgi-file=/home/lbw/apis/wsgi.py
processes=4
threads=2
master=true
buffer-size  = 88192
pidfile=uwsgi.pid
daemonzie=uwsgi.log
~

```
wsgi.py  


# Using
In you environment(python3.6)  

In devedeveloped environment  
$ python manage.py  

or in product environment  

$ uwsgi --ini uwsgi.ini  

### demo
try to open http://192.168.56.102:5000/apis_test

A simple ordinary least squares model.
http://192.168.56.102:5000/apis_statsmodels_ols/?x=[[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]&y=[2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]

Return json like 
![image](https://raw.githubusercontent.com/stjnu/statsmodels_json/master/app/static/images/ols.png)
Please visit https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html#statsmodels.regression.linear_model.OLS for json detail 
