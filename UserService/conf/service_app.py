import django
from flask import Flask
from flask_restful import Api
django.setup()
from UserService.service_api.ping import Ping
from UserService.service_api.user import User
app = Flask(__name__)

api= Api(app,prefix="/")

api.add_resource(Ping ,"ping/")
api.add_resource(User ,"user/")

if __name__ == "__main__":
    app.run(debug=True,port=5000,host="localhost")