
from flask import Blueprint
from flask import request,render_template,Response,make_response

from app.spc2 import *
import numpy as np

import pandas as pd
import sys
import json
from config import config


apis_spc_v1 = Blueprint('apis_spc_v1', __name__)

@apis_spc_v1.route('/')
def spc2(name=None):
    y = request.args.get('data')
    y = y.split(",")
    y = list(map(float, y))

    s = Spc_wxj(y, CHART_X_MR_X)
    s_MR = Spc_wxj(y, CHART_X_MR_MR)
    data_mr = s_MR.get_data_mr()

    i=0
    tmp=""
    v_num=0
    violating_points=s.get_violating_points()


    for key in violating_points:
        #print(key)
        #print(violating_points[key])
        #t=violating_points[key]
        #tmp =tmp + "\""+str(i)+"\":{\"name\":\""+key +"\",\"value\":\""+str(violating_points[key])+"\"},"
        tmp_vp=""
        for v in violating_points[key]:
            tmp_vp = tmp_vp + "["+ str(v) + ","+str(y[v])+"];"
        tmp_vp = tmp_vp[0:len(tmp_vp)-1]
        #tmp =tmp + "{\"name\": \"" + key + "\",\"value\": \"" +str(violating_points[key]) + "\"},"
        tmp =tmp + "{\"name\": \"" + key + "\",\"value\": \"" +tmp_vp + "\"},"
        v_num = i
        i=i+1
    tmp = tmp[0:len(tmp)-1]

    avg = s.center
    lcl = s.lcl
    ucl = s.ucl



    j=0
    tmp_mr=""
    v_num_mr=0
    violating_points=s_MR.get_violating_points()


    for key in violating_points:
        #print(key)
        #print(violating_points[key])
        #t=violating_points[key]
        #tmp_mr =tmp_mr + "\""+str(j)+"\":{\"name\":\""+key +"\",\"value\":\""+str(violating_points[key])+"\"},"

        tmp_mr =tmp_mr + "{\"name\": \"" + key + "\",\"value\": \"" +str(violating_points[key]) + "\"},"

        v_num_mr=j
        j=j+1
    tmp_mr = tmp_mr[0:len(tmp_mr)-1]

    avg_mr = s_MR.center
    lcl_mr = s_MR.lcl
    ucl_mr = s_MR.ucl


    # str1 = """[{
    #     "data": %s, 
    #     "UCL":%s,
    #     "LCL":%s,
    #     "AVG":%s,
    #     "violating_points":[{"num":1},{%s}],
    #     "data_mr":%s,
    #     "UCL_mr":%s,
    #     "LCL_mr":%s,
    #     "AVG_mr":%s,
    #     "violating_points_mr":{%s}

    # }]"""%(y,ucl,lcl,avg,tmp,data_mr,ucl_mr,lcl_mr,avg_mr,tmp_mr)



    str1 = """
    {
	  "origin": {
	    "data": %s,
	    "UCL": %s,
	    "LCL": %s,
	    "AVG": %s,
	    "violating_points": {
	      "num": %s,
	      "rusult": [%s]
	    }
	  },
	  "mr": {
	    "data": %s,
	    "UCL": %s,
	    "LCL": %s,
	    "AVG": %s,
	    "violating_points": {
	      "num": %s,
	      "rusult": [%s]
	    }
	  }

	}
	"""%(y,ucl,lcl,avg,v_num,tmp,data_mr,ucl_mr,lcl_mr,avg_mr,v_num_mr,tmp_mr)

    #return render_template('spc2.html', data=y,j=str1,tmp=tmp)
    #Response.headers['Access-Control-Allow-Origin'] = '*'


    return Response(str1, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.1:81",
    	"Access-Control-Allow-Methods":"GET",
    	"Access-Control-Allow-Headers":"x-requested-with,content-type",
    	"Access-Control-Allow-Credentials":"true"})
    #resp = make_response(render_template('spc2.html', data=y,j=str1,tmp=tmp), 200)
    #resp.headers['Content-Type'] = 'application/json'
    #return resp




