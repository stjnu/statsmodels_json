from flask import Blueprint

apis_test = Blueprint('apis_test', __name__)

@apis_test.route("/apis_test")
def fn_apis_test():
    return "apis_test"