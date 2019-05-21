
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password

fake = Faker()

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create=('email',)

    first_name = fake.first_name()
    last_name = fake.last_name()
    email=first_name+"."+last_name+"@opn.ninja"
    password = make_password(first_name)
    username = first_name+"_"+last_name

