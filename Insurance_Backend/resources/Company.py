from flask_restful import Resource
from flask import make_response, request,jsonify
from mongoengine.errors import DoesNotExist, ValidationError
from Insurance_Backend.documents import user_doc as Users_Doc
from Insurance_Backend.documents import company_doc as Company_Doc
import smtplib


class Company(Resource):

    def post(self):
        request_body = request.get_json()
        print(request_body)
        email = request_body['email']
        company_name = request_body['company_name']
        try :
            company1 = Company_Doc.Company.objects(email=email,company_name=company_name).first()

            if(company1):
                return make_response(jsonify({'message':'Company already exists','success':0}),401)

            else:
                company1=Company_Doc.Company(email=email,company_name=company_name)
                if('company_name' in request_body):
                    company1.first_name = request_body['company_name']
                if('contact_person' in request_body):
                    company1.contact_person = request_body['contact_person']
                if('company_email' in request_body):
                    company1.company_email = request_body['company_email']
                if('company_address' in request_body):
                    company1.address = request_body['company_address']
                if('products_required' in request_body):
                    company1.products_required = request_body['products_required']
                company1.save()
        except ValidationError as ve:
            print(str(ve))
            return make_response(jsonify({'message': "Validation error occured:" + str(ve), 'success': 0}), 404)
        except Exception as e:
            print(str(e))
            return make_response(jsonify({'message': "Error occured:" + str(e), 'success': 0}), 404)
        try:
            message_content="Please fill the below form \
                            http://localhost:4200/fillform"
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("perilwiseinsur123@gmail.com", "Perilwise1234$")
            server.sendmail("perilwiseinsur123@gmail.com", "arunashok22041996@gmail.com", "message")
            server.quit()
        except Exception as e:
            print(str(e))
            return make_response(jsonify({'message': "Company Added but email not sent!!",'success':0}),401)
        return make_response(jsonify({'message': "Company Added!!!", 'success': 1}), 200)


