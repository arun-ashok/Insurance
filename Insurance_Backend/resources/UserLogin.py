from flask_restful import Resource
from flask import make_response, request,jsonify
from mongoengine.errors import DoesNotExist, ValidationError
from Insurance.documents import user_doc as Doc
from Insurance.resources.token_jwt import encode_auth_token,decode_auth_token
from flask_httpauth import HTTPBasicAuth

class UserLogin(Resource):
    """
    This resource is for Creating user and Getting all users.
    """
    auth = HTTPBasicAuth()

    @auth.verify_password
    def verify_password(email, password):
        # Return UserDoc if username matches else None
        try:
            user1 = Doc.Users.objects(email=email).first()
            if (user1):
                if (user1.password == password):
                    return make_response(user1.to_json(), 200)
        except Exception as e:
            print(str(e))
            return make_response("Email not valid", 404)

    #@auth.login_required
    def post(self):
        request_body = request.get_json()
        print(request_body)
        try:
            user1=Doc.Users.objects(email=request_body['email']).first()
            print(user1)
            if(user1):
                if(user1.password==request_body['password']):
                    print("Login Successfull")
                    token=encode_auth_token(request_body['email'])
                    token=token.decode("utf-8")
                    print(str(token[1:]))
                    return make_response(jsonify({'token':str(token),'success':1,'username':user1.first_name}),200)
                else:
                    print("Wrong email/password")
                    return make_response(jsonify({'message':'Wrong email/password','success':0,}), 404)
            else:
                print("Wrong email/password")
                return make_response(jsonify({'message':'Wrong email/password','success':0}), 404)
        except Exception as e :
            print("Error")
            return make_response(jsonify({'message':'Wrong email/password','success':0}),404)