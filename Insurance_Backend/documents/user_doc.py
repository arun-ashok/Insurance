from mongoengine import Document, StringField, EmailField, IntField


class Users(Document):
    email = EmailField(required=True)
    password = StringField(required=True)
    first_name = StringField(required=True )
    last_name = StringField(required=True)
    phone = IntField(required=False,max_value=9999999999)