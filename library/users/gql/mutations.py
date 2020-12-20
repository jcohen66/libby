from graphene import Field, Mutation, String
from django.contrib.auth import get_user_model
from .types import UserType

User = get_user_model()

class UserCreate(Mutation):
    # 1. Declare the mutation arguments, result
    user = Field(UserType)

    # 2. Declare the args for our mutation
    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)

    
    # 3. Creae a new user model
    def mutate(self, info, username, password, email):
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return UserCreate(user=user)