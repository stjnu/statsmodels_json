from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_glsar = Blueprint('apis_statsmodels_glsar', __name__)

@apis_statsmodels_glsar.route("/")



def fn_apis_statsmodels_glsar():
    import numpy as np
    x = request.args.get('x')
    y = request.args.get('y')
    x1 = np.array(eval(x))
    y1 = np.array(eval(y))
    #x1 = [[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]
    #y1 = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]

    x1 = sm.add_constant(x1)
    model = sm.GLSAR(y1, x1)
    rs = model.fit()

        
    c = obj_rs(
        rs.aic,
        rs.bic,
        rs.bse.tolist(),
        rs.centered_tss,
        rs.condition_number,
        rs.conf_int().tolist(),
        rs.cov_HC0.tolist(),
        rs.cov_HC1.tolist(),
        rs.cov_HC2.tolist(),
        rs.cov_HC3.tolist(),
        rs.cov_kwds,
        rs.cov_params().tolist(),
        rs.cov_type,
        rs.df_model,
        rs.df_resid,
        rs.eigenvals.tolist(),
        rs.ess,
        rs.f_pvalue,
        rs.fittedvalues.tolist(),
        rs.fvalue,
        rs.k_constant,
        rs.llf,
        rs.mse_model,
        rs.mse_resid,
        rs.mse_total,
        rs.nobs,
        rs.normalized_cov_params.tolist(),
        rs.params.tolist(),
        rs.pvalues.tolist(),
        rs.resid.tolist(),
        rs.resid_pearson.tolist(),
        rs.rsquared,
        rs.rsquared_adj,
        rs.scale,
        rs.ssr,
        rs.tvalues.tolist(),
        rs.uncentered_tss,
        rs.use_t,
        rs.wresid.tolist()

         
         )

    c= c.__dict__


    tmp = json.dumps(c,ensure_ascii=False,indent=4)
    return Response(tmp, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.0:5000","Access-Control-Allow-Methods":"GET","Access-Control-Allow-Headers":"x-requested-with,content-type","Access-Control-Allow-Credentials":"true"})
    #return tmp

class obj_rs:
    aic = float
    bic = float
    bse = list
    centered_tss = float
    condition_number = float
    conf_int = list
    cov_HC0 = list
    cov_HC1 = list
    cov_HC2 = list
    cov_HC3 = list
    cov_kwds = list
    cov_params = list
    cov_type = str
    df_model = float
    df_resid = float
    eigenvals = list
    ess = float
    f_pvalue = float
    fittedvalues = list
    fvalue = float
    k_constant = int
    llf = float
    mse_model = float
    mse_resid = float
    mse_total = float
    nobs = float
    normalized_cov_params = list
    params = list
    pvalues = list
    resid = list
    resid_pearson = list
    rsquared = float
    rsquared_adj = float
    scale = float
    ssr = float
    tvalues = list
    uncentered_tss = float
    use_t = str
    wresid = list


    
    def __init__(self,
        aic,
        bic,
        bse,
        centered_tss,
        condition_number,
        conf_int,
        cov_HC0,
        cov_HC1,
        cov_HC2,
        cov_HC3,
        cov_kwds,
        cov_params,
        cov_type,
        df_model,
        df_resid,
        eigenvals,
        ess,
        f_pvalue,
        fittedvalues,
        fvalue,
        k_constant,
        llf,
        mse_model,
        mse_resid,
        mse_total,
        nobs,
        normalized_cov_params,
        params,
        pvalues,
        resid,
        resid_pearson,
        rsquared,
        rsquared_adj,
        scale,
        ssr,
        tvalues,
        uncentered_tss,
        use_t,
        wresid



                 ):
            self.aic = aic
            self.bic = bic
            self.bse = bse
            self.centered_tss = centered_tss
            self.condition_number = condition_number
            self.conf_int = conf_int
            self.cov_HC0 = cov_HC0
            self.cov_HC1 = cov_HC1
            self.cov_HC2 = cov_HC2
            self.cov_HC3 = cov_HC3
            self.cov_kwds = cov_kwds
            self.cov_params = cov_params
            self.cov_type = cov_type
            self.df_model = df_model
            self.df_resid = df_resid
            self.eigenvals = eigenvals
            self.ess = ess
            self.f_pvalue = f_pvalue
            self.fittedvalues = fittedvalues
            self.fvalue = fvalue
            self.k_constant = k_constant
            self.llf = llf
            self.mse_model = mse_model
            self.mse_resid = mse_resid
            self.mse_total = mse_total
            self.nobs = nobs
            self.normalized_cov_params = normalized_cov_params
            self.params = params
            self.pvalues = pvalues
            self.resid = resid
            self.resid_pearson = resid_pearson
            self.rsquared = rsquared
            self.rsquared_adj = rsquared_adj
            self.scale = scale
            self.ssr = ssr
            self.tvalues = tvalues
            self.uncentered_tss = uncentered_tss
            self.use_t = use_t
            self.wresid = wresid