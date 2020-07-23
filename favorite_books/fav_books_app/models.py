from django.db import models
from login_reg_app.models import User


class BookManager(models.Manager):
    def book_validator(self, form_data):
        errors = {}

        if len(form_data['title']) < 1:
            errors['title'] = "Title must not be blank."
        if len(form_data['description']) < 5:
            errors['description'] = "Description must at least 5 characters long."

        return errors


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='liked_books',)

    objects = BookManager()
