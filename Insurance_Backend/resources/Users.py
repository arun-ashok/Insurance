from flask_restful import Resource
from flask import make_response, request,jsonify
from mongoengine.errors import DoesNotExist, ValidationError
from Insurance_Backend.documents import user_doc as Doc
#from werkzeug.security import generate_password_hash, check_password_hash
#from Insurance.resources.validations import validate_user
from flask_httpauth import HTTPBasicAuth
import uuid

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    # Return UserDoc if username matches else None
    print(email)
    print(password)
    try:
        user1 = Doc.Users.objects(email=email).first()
        if (user1):
            if(user1.password==password):
                return make_response(user1.to_json(), 200)
    except Exception as e:
        print(str(e))
        return make_response("Username not valid", 404)


class Users(Resource):
    """
    This resource is for Creating user and Getting all users.
    """

    #@auth.login_required
    def get(self):

        # if username matches return all meals of the user
        users_list = Doc.Users.objects().exclude("id").all()
        print(users_list)
        users_json = [user.to_json() for user in users_list]
        print(users_list.to_json())
        return make_response(users_list.to_json(), 200)

    # Creates new user and persists in MongoDB
    def post(self):
        request_body = request.get_json()
        email=request_body['email']
        password=request_body['password']
        print(request_body)
        print("Reached")
        try:
            user1 = Doc.Users.objects(email=email).first()
            if(user1):
                print("Already registered with this email")
                return make_response(jsonify({'message':"Already registered with this email", 'success': 0}), 400)
        except Exception as e:
            print("Exception")
            print(str(e))
            return make_response(jsonify({'message': "Already registered with this email", 'success': 0}), 400)

        try:
            user1=Doc.Users(email=email,password=password)
            if('firstname' in request_body):
                user1.first_name = request_body['firstname']
            if('lastname' in request_body):
                user1.last_name=request_body['lastname']
            if('phone' in request_body):
                user1.phone=request_body['phone']

            user1.save()
            print("Saved")
            print(user1)

        except ValidationError as ve:
            print(str(ve))
            return make_response(jsonify({'message':"Validation error occured:"+str(ve),'success':0}),404)
        except Exception as e:
            print(str(e))
        print(Doc.Users.objects)
        return make_response(jsonify({'message':"User Added!!!",'success':1}),200)
