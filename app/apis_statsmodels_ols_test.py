from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_ols_test = Blueprint('apis_statsmodels_ols_test', __name__)

@apis_statsmodels_ols_test.route("/")



def fn_apis_statsmodels_ols_test():
	import numpy as np

	x1 = [[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]
	y1 = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]
 
	x1 = sm.add_constant(x1)
	model = sm.OLS(y1, x1)
	rs = model.fit()

	#对象初始化
	c =obj_rs(
	    rs.HC0_se.tolist(),
	    rs.aic,
	    rs.bic,
	    rs.bse.tolist()

	     )
	
	c= c.__dict__


	tmp = json.dumps(c,ensure_ascii=False,indent=4)
	return Response(tmp, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.0:5000","Access-Control-Allow-Methods":"GET","Access-Control-Allow-Headers":"x-requested-with,content-type","Access-Control-Allow-Credentials":"true"})
	#return tmp

class obj_rs:
    HC0_se = list
    aic = float
    bic = float
    bse = list
    def __init__(self, HC0_se,aic,bic,bse,):
        self.HC0_se = HC0_se
        self.aic = aic
        self.bic = bic
        self.bse = bse