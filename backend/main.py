from flask import Flask, Response, make_response
from flasgger import Swagger
import logging
import sys
sys.path.append('.')

from orm.OrmEntities import db
from controller.routers import routers
from exceptions.ExceptionHandler import exceptionHandler
from exceptions.ExceptionEntity import ExceptionEntity

app = Flask(__name__) 

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'APISpecification',
            "route": '/APISpecification',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "specs_route": "/swagger_doc/",
}

Swagger(app, config=swagger_config)

# init db using pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://debian-sys-maint:gRkBnPZiKqbwiV6h@localhost/test'
# create tables, remove in production
with app.app_context():
    db.init_app(app)
    db.create_all()

# define routers
app.register_blueprint(routers, url_prefix="/") 

# cors
@app.after_request
def func_res(resp):     
    res = make_response(resp)
    print(res.status)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS,DELETE,PUT'
    res.headers['Access-Control-Allow-Headers'] = '*'
    return res

# define logger
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# define exception handlers
# @app.errorhandler(Exception)
def handle_exception(e):
    # process exceptions
    res: ExceptionEntity = exceptionHandler(e)
    response = Response(res.msg, res.code)
    # construct response json data
    response.data = res.to_json()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.content_type = "application/json"
    return response

if __name__ == '__main__': 
  app.run(host="0.0.0.0", port='8080')
