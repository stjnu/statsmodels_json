from flask import Blueprint

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from flask import request,render_template,Response,make_response
import json
apis_statsmodels_recursive_ls = Blueprint('apis_statsmodels_recursive_ls', __name__)

@apis_statsmodels_recursive_ls.route("/")



def fn_apis_statsmodels_recursive_ls():
    import numpy as np
    x = request.args.get('x')
    y = request.args.get('y')
    x1 = np.array(eval(x))
    y1 = np.array(eval(y))
    #x1 = [[4,67,662],[9,19,618],[6,49,372],[6,33,58],[1,18,153],[2,78,938],[3,15,627],[8,55,191],[2,47,812],[2,83,946],[2,4,895],[9,37,42],[0,1,595],[7,27,392],[5,22,836],[0,12,513],[2,41,601],[3,68,615],[2,23,649],[1,98,9],[9,40,32],[5,77,798],[1,10,903],[1,53,772],[7,20,716],[2,35,678],[5,52,258],[7,31,814],[2,30,577]]
    #y1 = [2857.0163,2547.5962,1647.6061,343.8966,668.2108,3990.0414,2559.0662,945.1439,3393.1068,4037.1068,3596.0458,297.5798,2383.6193,1663.8839,3420.5135,2088.0197,2531.2703,2670.7878,2669.8044,332.9981,266.718,3433.975,3644.3636,3249.3518,2938.0325,2821.3308,1198.4373,3363.5752,2402.6042]
 
    x1 = sm.add_constant(x1)
    model = sm.RecursiveLS(y1, x1)
    rs = model.fit()

    c =rs_ols(
        rs.aic,
        rs.bic,
        rs.bse.tolist(),
        rs.conf_int().tolist(),
        rs.cov_kwds,
        rs.cov_params().tolist(),
        rs.cov_params_approx.tolist(),
        rs.cov_params_default.tolist(),
        rs.cov_params_oim.tolist(),
        rs.cov_params_opg.tolist(),
        rs.cov_params_robust.tolist(),
        rs.cov_params_robust_approx.tolist(),
        rs.cov_params_robust_oim.tolist(),
        rs.cov_type,
        rs.cusum.tolist(),
        rs.cusum_squares.tolist(),
        rs.data_in_cache,
        rs.df_resid,
        rs.filtered_state.tolist(),
        rs.filtered_state_cov.tolist(),
        rs.fittedvalues.tolist(),
        rs.forecasts.tolist(),
        rs.forecasts_error.tolist(),
        rs.forecasts_error_cov.tolist(),
        rs.hqic,
        rs.k_constant,
        rs.llf,
        rs.llf_obs.tolist(),
        rs.loglikelihood_burn,
        rs.nobs,
        rs.params.tolist(),
        rs.predict().tolist(),
        rs.predicted_state.tolist(),
        rs.predicted_state_cov.tolist(),
        rs.pvalues.tolist(),
        rs.resid.tolist(),
        rs.resid_recursive.tolist(),
        rs.scale,
        rs.smoothed_measurement_disturbance.tolist(),
        rs.smoothed_measurement_disturbance_cov.tolist(),
        rs.smoothed_state.tolist(),
        rs.smoothed_state_cov.tolist(),
        rs.smoothed_state_disturbance.tolist(),
        rs.smoothed_state_disturbance_cov.tolist(),
        rs.tvalues.tolist(),
        rs.use_t,
        rs.zvalues.tolist(),
  

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
    cov_kwds = list
    cov_params = list
    cov_params_approx = list
    cov_params_default = list
    cov_params_oim = list
    cov_params_opg = list
    cov_params_robust = list
    cov_params_robust_approx = list
    cov_params_robust_oim = list
    cov_type = str
    cusum = list
    cusum_squares = list
    data_in_cache = list
    df_resid = float
    filtered_state = list
    filtered_state_cov = list
    fittedvalues = list
    forecasts = list
    forecasts_error = list
    forecasts_error_cov = list
    hqic = float
    k_constant = int
    llf = float
    llf_obs = list
    loglikelihood_burn = int
    nobs = int
    params = list
    predict = list
    predicted_state = list
    predicted_state_cov = list
    pvalues = list
    resid = list
    resid_recursive = list
    scale = float
    smoothed_measurement_disturbance = list
    smoothed_measurement_disturbance_cov = list
    smoothed_state = list
    smoothed_state_cov = list
    smoothed_state_disturbance = list
    smoothed_state_disturbance_cov = list
    tvalues = list
    use_t = str
    zvalues = list






    
    def __init__(self,
        aic,
        bic,
        bse,
        conf_int,
        cov_kwds,
        cov_params,
        cov_params_approx,
        cov_params_default,
        cov_params_oim,
        cov_params_opg,
        cov_params_robust,
        cov_params_robust_approx,
        cov_params_robust_oim,
        cov_type,
        cusum,
        cusum_squares,
        data_in_cache,
        df_resid,
        filtered_state,
        filtered_state_cov,
        fittedvalues,
        forecasts,
        forecasts_error,
        forecasts_error_cov,
        hqic,
        k_constant,
        llf,
        llf_obs,
        loglikelihood_burn,
        nobs,
        params,
        predict,
        predicted_state,
        predicted_state_cov,
        pvalues,
        resid,
        resid_recursive,
        scale,
        smoothed_measurement_disturbance,
        smoothed_measurement_disturbance_cov,
        smoothed_state,
        smoothed_state_cov,
        smoothed_state_disturbance,
        smoothed_state_disturbance_cov,
        tvalues,
        use_t,
        zvalues,




                 ):
        self.aic = aic
        self.bic = bic
        self.bse = bse
        self.conf_int = conf_int
        self.cov_kwds = cov_kwds
        self.cov_params = cov_params
        self.cov_params_approx = cov_params_approx
        self.cov_params_default = cov_params_default
        self.cov_params_oim = cov_params_oim
        self.cov_params_opg = cov_params_opg
        self.cov_params_robust = cov_params_robust
        self.cov_params_robust_approx = cov_params_robust_approx
        self.cov_params_robust_oim = cov_params_robust_oim
        self.cov_type = cov_type
        self.cusum = cusum
        self.cusum_squares = cusum_squares
        self.data_in_cache = data_in_cache
        self.df_resid = df_resid
        self.filtered_state = filtered_state
        self.filtered_state_cov = filtered_state_cov
        self.fittedvalues = fittedvalues
        self.forecasts = forecasts
        self.forecasts_error = forecasts_error
        self.forecasts_error_cov = forecasts_error_cov
        self.hqic = hqic
        self.k_constant = k_constant
        self.llf = llf
        self.llf_obs = llf_obs
        self.loglikelihood_burn = loglikelihood_burn
        self.nobs = nobs
        self.params = params
        self.predict = predict
        self.predicted_state = predicted_state
        self.predicted_state_cov = predicted_state_cov
        self.pvalues = pvalues
        self.resid = resid
        self.resid_recursive = resid_recursive
        self.scale = scale
        self.smoothed_measurement_disturbance = smoothed_measurement_disturbance
        self.smoothed_measurement_disturbance_cov = smoothed_measurement_disturbance_cov
        self.smoothed_state = smoothed_state
        self.smoothed_state_cov = smoothed_state_cov
        self.smoothed_state_disturbance = smoothed_state_disturbance
        self.smoothed_state_disturbance_cov = smoothed_state_disturbance_cov
        self.tvalues = tvalues
        self.use_t = use_t
        self.zvalues = zvalues