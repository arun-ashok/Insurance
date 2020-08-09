from mongoengine import Document, StringField, EmailField, IntField


class Users(Document):
    email = EmailField(required=False)
    password = StringField(required=True)
    first_name = StringField(required=False)
    last_name = StringField(required=False)
    phone = IntField(required=False,max_value=9999999999)