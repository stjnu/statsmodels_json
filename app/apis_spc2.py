
from flask import Blueprint
from flask import request,render_template,Response,make_response

from app.spc2 import *
import numpy as np

import pandas as pd
import sys
import json
from config import config


apis_spc_v2 = Blueprint('apis_spc_v2', __name__)

@apis_spc_v2.route('/')
def spc2(name=None):
    y = request.args.get('data')
    y = y.split(",")
    y = list(map(float, y))

    s = Spc_wxj(y, CHART_X_MR_X)
    s_MR = Spc_wxj(y, CHART_X_MR_MR)




    str1 = """
    {
	  "origin": {
	    "data":[111],
	    "UCL": 222


	  }

	}
	"""
    j1=json.dumps(s.__dict__,ensure_ascii=False,indent=4)

    #return render_template('spc2.html', data=y,j=str1,tmp=tmp)
    #Response.headers['Access-Control-Allow-Origin'] = '*'


    return Response(j1, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.1:81",
    	"Access-Control-Allow-Methods":"GET",
    	"Access-Control-Allow-Headers":"x-requested-with,content-type",
    	"Access-Control-Allow-Credentials":"true"})
    #resp = make_response(render_template('spc2.html', data=y,j=str1,tmp=tmp), 200)
    #resp.headers['Content-Type'] = 'application/json'
    #return resp




