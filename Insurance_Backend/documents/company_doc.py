from mongoengine import Document, StringField, EmailField, IntField,ListField

class Company(Document):
    email = EmailField(required=True)
    company_name = StringField(required=True)
    contact_person = StringField(required=True)
    company_email = EmailField(required=True)
    address = StringField(required=True)
    products_required = ListField(required=False)


