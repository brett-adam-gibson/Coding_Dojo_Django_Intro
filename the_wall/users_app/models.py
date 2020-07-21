import re
from django.db import models
import bcrypt

# Create your models here.
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def get_all_by_email(self):
        return self.order_by('email')

    def register(self, form_data):
        my_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            password=my_hash,
            email=form_data['email'],
        )

    def authenticate(self, email, password):
        # return True/False
        users_with_email = self.filter(email=email)
        if not users_with_email:
            return False
        user = users_with_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def validate(self, form_data):

        errors = {}
        if len(form_data['first_name']) < 1:
            errors['first_name'] = 'First Name field is required.'

        if len(form_data['last_name']) < 1:
            errors['last_name'] = 'Last Name field is required.'

        if len(form_data['email']) < 1:
            errors['email'] = 'Email field is required.'

        if not EMAIL_MATCH.match(form_data['email']):
            errors['email'] = 'Invalid Email.'

        if form_data['password'] != form_data['confirm']:
            errors['password'] = "Passwords do not match"

        # prevent duplicate emails!
        users_with_email = self.filter(email=form_data['email'])
        if users_with_email: # if NON-EMPTY list
            errors['email'] = 'Email already in use.'

        return errors

class User(models.Model):
    # id = 1
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    #posts
    # denys.posts.all()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
