
from flask import Flask
#import buleprint from app/*.py files

from app.apis_test import apis_test
from app.apis_spc import apis_spc_v1
from app.apis_spc2 import apis_spc_v2
from app.apis_statsmodels_glm import apis_statsmodels_glm
from app.apis_statsmodels_ols import apis_statsmodels_ols
from app.apis_statsmodels_wls import apis_statsmodels_wls
from app.apis_statsmodels_glsar import apis_statsmodels_glsar
from app.apis_statsmodels_rlm import apis_statsmodels_rlm


from app.apis_statsmodels_ols_test import apis_statsmodels_ols_test

#from config import config

app = Flask(__name__)
#Define access base URL for every bluesprint,for example,if there is  @apis_statsmodels_glm.route("/test") in the app/apis_statsmodels_glm.py file,you can access http://127.0.0.1:5000//apis_statsmodels_glm/test/
app.register_blueprint(apis_test)
app.register_blueprint(apis_spc_v2,url_prefix='/apis_spc_v2')
app.register_blueprint(apis_spc_v1,url_prefix='/apis_spc_v1')
app.register_blueprint(apis_statsmodels_ols,url_prefix='/apis_statsmodels_ols')
app.register_blueprint(apis_statsmodels_glm,url_prefix='/apis_statsmodels_glm')
app.register_blueprint(apis_statsmodels_wls,url_prefix='/apis_statsmodels_wls')
app.register_blueprint(apis_statsmodels_glsar,url_prefix='/apis_statsmodels_glsar')
app.register_blueprint(apis_statsmodels_rlm,url_prefix='/apis_statsmodels_rlm')


app.register_blueprint(apis_statsmodels_ols_test,url_prefix='/apis_statsmodels_ols_test')



#app.config.from_object(config)
if __name__ == "__main__":
    app.run()