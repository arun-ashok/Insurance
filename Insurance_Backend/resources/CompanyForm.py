from flask_restful import Resource
from flask import make_response, request,jsonify
from mongoengine.errors import DoesNotExist, ValidationError
#from Insurance_Backend.documents import user_doc as Users_Doc
from Insurance_Backend.documents import form_doc as Form_Doc


class CompanyForm(Resource):
    def get(self):
        email = request.args.get('email')
        print(email)
        forms_list = Form_Doc.Form.objects(email=email).exclude("id").all()
        print(forms_list)
        forms_json = [form.to_json() for form in forms_list]
        print(forms_list.to_json())
        return make_response(forms_list.to_json(), 200)

    def post(self):
        request_body = request.get_json()
        print(request_body)
        email = request_body['email']
        company_email=request_body['company_email']
        try :
            company1 = Form_Doc.Form.objects(email=email,company_email=company_email).first()
            a1 = request_body['a1']
            a2=request_body['a2']
            a3=request_body['a3']
            a4 = request_body['a4']
            a5 = request_body['a5']
            a6 = request_body['a6']
            a7 = request_body['a7']
            a8 = request_body['a8']
            a9 = request_body['a9']
            a10 = request_body['a10']
            a11 = request_body['a11']
            a12 = request_body['a12']
            a13 = request_body['a13']
            a14 = request_body['a14']
            a15 = request_body['a15']
            a16 =request_body['a16']
            a17 = request_body['a17']
            a18 = request_body['a18']
            a19 = request_body['a19']
            a20 = request_body['a20']
            a21 = request_body['a21']
            a22 = request_body['a22']
            b1 = request_body['b1']
            b2 = request_body['b2']
            b3 = request_body['b3']
            b4 = request_body['b4']
            b5 = request_body['b5']
            b6 = request_body['b6']
            b7 = request_body['b7']
            b8 = request_body['b8']

            if(company1):
                return make_response(jsonify({'message':'Form already exists','success':0}),401)

            else:
                form1 = Form_Doc.Form(email=email,company_email=company_email,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,
                                               a10=a10,a11=a11,a12=a12,a13=a13,a14=a14,a15=a15,a16=a16,a17=a17,a18=a18,
                                               a19=a19,a20=a20,a21=a21,a22=a22,b1=b1,b2=b2,b3=b3,b4=b4,b5=b5,b6=b6,b7=b7,b8=b8)
                form1.save()
        except ValidationError as ve:
            print(str(ve))
            return make_response(jsonify({'message': "Validation error occured:" + str(ve), 'success': 0}), 404)
        except Exception as e:
            print(str(e))
            return make_response(jsonify({'message': "Error occured:" + str(e), 'success': 0}), 404)
        return make_response(jsonify({'message': "Form Added!!!", 'success': 1}), 200)

