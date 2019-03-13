from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_rlm = Blueprint('apis_statsmodels_rlm', __name__)

@apis_statsmodels_rlm.route("/")



def fn_apis_statsmodels_rlm():
    import numpy as np
    x = request.args.get('x')
    y = request.args.get('y')
    x1 = np.array(eval(x))
    y1 = np.array(eval(y))
    #x1 = [[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]
    #y1 = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]

    x1 = sm.add_constant(x1)
    model = sm.RLM(y1, x1)
    rs = model.fit()

        
    c = obj_rs(
        rs.bcov_scaled.tolist(),
        rs.bcov_unscaled.tolist(),
        rs.bse.tolist(),
        rs.chisq.tolist(),
        rs.conf_int().tolist(),
        rs.cov_params().tolist(),
        rs.cov_params_default.tolist(),
        rs.data_in_cache,
        rs.df_model,
        rs.df_resid,
        rs.fit_history['deviance'],
        rs.fit_history['iteration'],
        #rs.fit_history['params'][1],
        rs.fit_history['scale'],
        
            
                
        rs.fit_options,
        rs.fittedvalues.tolist(),
        rs.k_constant,
        rs.nobs,
        rs.normalized_cov_params.tolist(),
        rs.params.tolist(),
        rs.predict().tolist(),
        rs.pvalues.tolist(),
        rs.resid.tolist(),
        rs.scale,
        rs.sresid.tolist(),
        rs.tvalues.tolist(),
        rs.use_t,
        rs.weights.tolist()

         )

    c= c.__dict__


    tmp = json.dumps(c,ensure_ascii=False,indent=4)
    return Response(tmp, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.0:5000","Access-Control-Allow-Methods":"GET","Access-Control-Allow-Headers":"x-requested-with,content-type","Access-Control-Allow-Credentials":"true"})
    #return tmp


class obj_rs:
    bcov_scaled = list
    bcov_unscaled = list
    bse = list
    chisq = list
    conf_int = list
    cov_params = list
    cov_params_default = list
    data_in_cache = list
    df_model = float
    df_resid = float
    
    fit_history_deviance = list
    fit_history_iteration = list
    #fit_history_params = list
    fit_history_scale = list



    fit_options = list
    fittedvalues = list
    k_constant = int
    nobs = float
    normalized_cov_params = list
    params = list
    predict = list
    pvalues = list
    resid = list
    scale = float
    sresid = list
    tvalues = list
    use_t = str
    weights = list

    
    def __init__(self,
        bcov_scaled,
        bcov_unscaled,
        bse,
        chisq,
        conf_int,
        cov_params,
        cov_params_default,
        data_in_cache,
        df_model,
        df_resid,
        
        fit_history_deviance,
        fit_history_iteration,
        #fit_history_params,
        fit_history_scale,
        
        fit_options,
        fittedvalues,
        k_constant,
        nobs,
        normalized_cov_params,
        params,
        predict,
        pvalues,
        resid,
        scale,
        sresid,
        tvalues,
        use_t,
        weights


                 ):
            self.bcov_scaled = bcov_scaled
            self.bcov_unscaled = bcov_unscaled
            self.bse = bse
            self.chisq = chisq
            self.conf_int = conf_int
            self.cov_params = cov_params
            self.cov_params_default = cov_params_default
            self.data_in_cache = data_in_cache
            self.df_model = df_model
            self.df_resid = df_resid
            
            self.fit_history_deviance = fit_history_deviance
            self.fit_history_iteration = fit_history_iteration
            #self.fit_history_params = fit_history_params
            self.fit_history_scale = fit_history_scale
            
            self.fit_options = fit_options
            self.fittedvalues = fittedvalues
            self.k_constant = k_constant
            self.nobs = nobs
            self.normalized_cov_params = normalized_cov_params
            self.params = params
            self.predict = predict
            self.pvalues = pvalues
            self.resid = resid
            self.scale = scale
            self.sresid = sresid
            self.tvalues = tvalues
            self.use_t = use_t
            self.weights = weights