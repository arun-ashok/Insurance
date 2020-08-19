# using flask_restful

from flask import Flask
from flask_restful import Api
from mongoengine import *
from Insurance_Backend.resources.UserLogin import UserLogin
from Insurance_Backend.resources.Users import Users
from Insurance_Backend.resources.Company import Company
from Insurance_Backend.resources.CompanyForm import CompanyForm
from flask_cors import CORS

#from mongoengine import connect

# https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html <-- Reference doc

# creating the flask app
app = Flask(__name__)
CORS(app)
# creating an API object
api = Api(app)


api.add_resource(UserLogin,'/perilwise/v1/user/login')
api.add_resource(Users, '/perilwise/v1/users')
api.add_resource(Company,'/perilwise/v1/company')
api.add_resource(CompanyForm,'/perilwise/v1/companyform')


# driver function
if __name__ == '__main__':
    connect('perilwise', host='localhost', port=27017)
    app.run(debug=True)