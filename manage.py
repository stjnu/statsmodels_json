
from flask import Flask
#引入app目录下的apis文件，并引入对象
from app.apis_test import apis_test
from app.apis_spc import apis_spc_v1
from app.apis_spc2 import apis_spc_v2
from app.apis_statsmodels_glm import apis_statsmodels_glm
from app.apis_statsmodels_ols import apis_statsmodels_ols

#from config import config

app = Flask(__name__)
#从对应的对象创建的蓝图，在app中注册，这样就可以通过蓝图指定的url访问了
app.register_blueprint(apis_test)


app.register_blueprint(apis_spc_v2,url_prefix='/apis_spc_v2')  #当我们在应用对象上注册一个蓝图时，可以指定一个url_prefix关键字参数（这个参数默认是/）
app.register_blueprint(apis_spc_v1,url_prefix='/apis_spc_v1')  #当我们在应用对象上注册一个蓝图时，可以指定一个url_prefix关键字参数（这个参数默认是/）

app.register_blueprint(apis_statsmodels_ols)
app.register_blueprint(apis_statsmodels_glm,url_prefix='/apis_statsmodels_glm')



#app.config.from_object(config)
if __name__ == "__main__":
    app.run()