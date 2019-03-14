from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_ar = Blueprint('apis_statsmodels_ar', __name__)

@apis_statsmodels_ar.route("/")



def fn_apis_statsmodels_ar():
    import numpy as np
    x = request.args.get('x')

    maxlag = int(request.args.get('maxlag'))
    method = request.args.get('method')
    ic = request.args.get('ic')
    trend = request.args.get('trend')

    x = np.array(eval(x))
    #x = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]
    
    maxlag = 4 #request
    
    #ic=None #str {'aic','bic',','t-stat',None} default None
    ic_list = ['aic','bic','t-stat']
    if not(ic in ic_list): ic = None

    #trend='c' #str {'c','nc'} defalut c
    if trend != 'c' :trend = 'c'
    
    #method = 'cmle' #str {'cmle', 'mle'} default cmle
    if method!='mle':method='cmle'


    #maxlag (int) – If ic is None, then maxlag is the lag length used in fit. If ic is specified then maxlag is the highest lag order used to select the correct lag order. If maxlag is None, the default is round(12*(nobs/100.)**(1/4.))
    #method (str {'cmle', 'mle'}, optional) – cmle - Conditional maximum likelihood using OLS mle - Unconditional (exact) maximum likelihood. See solver and the Notes.
    #ic (str {'aic','bic','hic','t-stat'}) – Criterion used for selecting the optimal lag length. aic - Akaike Information Criterion bic - Bayes Information Criterion t-stat - Based on last lag hqic - Hannan-Quinn Information Criterion If any of the information criteria are selected, the lag length which results in the lowest value is selected. If t-stat, the model starts with maxlag and drops a lag until the highest lag has a t-stat that is significant at the 95 % level.
    #trend (str {'c','nc'}) – Whether to include a constant or not. ‘c’ - include constant. ‘nc’ - no constant.
    model = sm.tsa.AR(x)
    rs = model.fit(maxlag = maxlag,method = method,ic = ic,trend = trend )

    c =rs_ols(
        rs.aic,
        rs.bic,
        rs.bse.tolist(),
        rs.conf_int().tolist(),
        rs.cov_params().tolist(),
        rs.df_model,
        rs.df_resid,
        rs.extra_doc,
        rs.fittedvalues.tolist(),
        rs.fpe,
        rs.hqic,
        rs.k_ar,
        rs.k_constant,
        rs.k_trend,
        rs.llf,
        rs.n_totobs,
        rs.nobs,
        rs.normalized_cov_params.tolist(),
        rs.params.tolist(),
        rs.preddoc,
        rs.predict().tolist(),
        rs.pvalues.tolist(),
        rs.resid.tolist(),
        #rs.roots.tolist(), #TypeError: (0.19306374392626155-1.7070404685909495j) is not JSON serializable
        rs.scale,
        rs.sigma2,
        rs.summary(),
        rs.trendorder,
        rs.tvalues.tolist(),
        rs.use_t
  

         )

    c= c.__dict__


    tmp = json.dumps(c,ensure_ascii=False,indent=4)
    return Response(tmp, mimetype='application/json',headers={"Access-Control-Allow-Origin":"http://127.0.0.0:5000","Access-Control-Allow-Methods":"GET","Access-Control-Allow-Headers":"x-requested-with,content-type","Access-Control-Allow-Credentials":"true"})
    #return tmp

class rs_ols:
    aic = float
    bic = float
    bse = list
    conf_int = list
    cov_params = list
    df_model = int
    df_resid = int
    extra_doc = list
    fittedvalues = list
    fpe = float
    hqic = float
    k_ar = int
    k_constant = int
    k_trend = int
    llf = float
    n_totobs = int
    nobs = int
    normalized_cov_params = list
    params = list
    preddoc = list
    predict = list
    pvalues = list
    resid = list
    #roots = list
    scale = float
    sigma2 = float
    summary = list
    trendorder = int
    tvalues = list
    use_t = str


    
    def __init__(self,
        aic,
        bic,
        bse,
        conf_int,
        cov_params,
        df_model,
        df_resid,
        extra_doc,
        fittedvalues,
        fpe,
        hqic,
        k_ar,
        k_constant,
        k_trend,
        llf,
        n_totobs,
        nobs,
        normalized_cov_params,
        params,
        preddoc,
        predict,
        pvalues,
        resid,
        #roots,
        scale,
        sigma2,
        summary,
        trendorder,
        tvalues,
        use_t,


                 ):
        self.aic = aic
        self.bic = bic
        self.bse = bse
        self.conf_int = conf_int
        self.cov_params = cov_params
        self.df_model = df_model
        self.df_resid = df_resid
        self.extra_doc = extra_doc
        self.fittedvalues = fittedvalues
        self.fpe = fpe
        self.hqic = hqic
        self.k_ar = k_ar
        self.k_constant = k_constant
        self.k_trend = k_trend
        self.llf = llf
        self.n_totobs = n_totobs
        self.nobs = nobs
        self.normalized_cov_params = normalized_cov_params
        self.params = params
        self.preddoc = preddoc
        self.predict = predict
        self.pvalues = pvalues
        self.resid = resid
        #self.roots = roots
        self.scale = scale
        self.sigma2 = sigma2
        self.summary = summary
        self.trendorder = trendorder
        self.tvalues = tvalues
        self.use_t = use_t