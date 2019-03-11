from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_glm = Blueprint('apis_statsmodels_glm', __name__)

@apis_statsmodels_glm.route("/")



def fn_apis_statsmodels_glm():
	import numpy as np
	x = request.args.get('x')
	y = request.args.get('y')
	x1 = np.array(eval(x))
	y1 = np.array(eval(y))
	#x1 = [[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]
	#y1 = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]
 
	x1 = sm.add_constant(x1)
	model = sm.GLM(y1, x1)
	rs = model.fit()

        
	#对象初始化
	c =rs_ols(
		rs.aic,
		rs.bic,
		rs.deviance,
		rs.llf,
		rs.llnull,
		rs.null_deviance,
		rs.pearson_chi2,
		rs.scale,
		rs.k_constant,
		rs.nobs,
		int(rs.df_model),
		int(rs.df_resid),
		#rs.fit_history,
		rs.bse.tolist(),
		rs.data_in_cache,
		rs.fittedvalues.tolist(),
		rs.mu.tolist(),
		rs.normalized_cov_params.tolist(),
		rs.null.tolist(),
		rs.params.tolist(),
		#rs.pinv_wexog.tolist(),
		rs.pvalues.tolist(),
		rs.resid_anscombe.tolist(),
		rs.resid_deviance.tolist(),
		rs.resid_pearson.tolist(),
		rs.resid_response.tolist(),
		rs.resid_working.tolist(),
		rs.tvalues.tolist(),
		rs.conf_int().tolist(),
		rs.cov_params().tolist(),
		rs.predict().tolist(),
		rs.converged,
		rs.use_t,
		rs.cov_kwds,
		rs.cov_type,
		rs.method

		 
		 )
	#对象序列化
	c= c.__dict__


	tmp = json.dumps(c,ensure_ascii=False,indent=4)
	return Response(tmp, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.0:5000","Access-Control-Allow-Methods":"GET","Access-Control-Allow-Headers":"x-requested-with,content-type","Access-Control-Allow-Credentials":"true"})
	#return tmp

#定义对象
class rs_ols:
    aic = float
    bic = float
    deviance = float
    llf = float
    llnull = float
    null_deviance = float
    pearson_chi2 = float
    scale = float
    k_constant = int
    nobs = int
    df_model = int
    df_resid = int
    #fit_history = list
    bse = list
    data_in_cache = list
    fittedvalues = list
    mu = list
    normalized_cov_params = list
    null = list
    params = list
    #pinv_wexog = list
    pvalues = list
    resid_anscombe = list
    resid_deviance = list
    resid_pearson = list
    resid_response = list
    resid_working = list
    tvalues = list
    conf_int = list
    cov_params = list
    predict = list
    converged = str
    use_t = str
    cov_kwds = str
    cov_type = str
    method = str




    
    def __init__(self,
        aic,
        bic,
        deviance,
        llf,
        llnull,
        null_deviance,
        pearson_chi2,
        scale,
        k_constant,
        nobs,
        df_model,
        df_resid,
        #fit_history,
        bse,
        data_in_cache,
        fittedvalues,
        mu,
        normalized_cov_params,
        null,
        params,
        #pinv_wexog,
        pvalues,
        resid_anscombe,
        resid_deviance,
        resid_pearson,
        resid_response,
        resid_working,
        tvalues,
        conf_int,
        cov_params,
        predict,
        converged,
        use_t,
        cov_kwds,
        cov_type,
        method


                 ):
            self.aic = aic
            self.bic = bic
            self.deviance = deviance
            self.llf = llf
            self.llnull = llnull
            self.null_deviance = null_deviance
            self.pearson_chi2 = pearson_chi2
            self.scale = scale
            self.k_constant = k_constant
            self.nobs = nobs
            self.df_model = df_model
            self.df_resid = df_resid
            #self.fit_history = fit_history
            self.bse = bse
            self.data_in_cache = data_in_cache
            self.fittedvalues = fittedvalues
            self.mu = mu
            self.normalized_cov_params = normalized_cov_params
            self.null = null
            self.params = params
            #self.pinv_wexog = pinv_wexog
            self.pvalues = pvalues
            self.resid_anscombe = resid_anscombe
            self.resid_deviance = resid_deviance
            self.resid_pearson = resid_pearson
            self.resid_response = resid_response
            self.resid_working = resid_working
            self.tvalues = tvalues
            self.conf_int = conf_int
            self.cov_params = cov_params
            self.predict = predict
            self.converged = converged
            self.use_t = use_t
            self.cov_kwds = cov_kwds
            self.cov_type = cov_type
            self.method = method


