from datetime import datetime
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def form_validation(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'Title should be atleast 2 characters.'

        if len(post_data['network']) < 3:
            errors['network'] = 'Network should be atleast 3 characters.'

        if len(post_data['description']) != 0 and len(post_data['description']) < 10:
            errors['description'] = 'Description should be atleast 10 characters.'

        if post_data['release_date'] == '':
            errors['release_date'] = 'Release Date is missing.'

        shows_with_title = self.filter(title=post_data['title'])
        if shows_with_title:
            errors['title'] = 'Show already exists.'

        else:
            date = datetime.strptime(post_data['release_date'], '%Y-%m-%d')
            if date > datetime.now():
                errors['release_date'] = 'Date needs to be in the past.'

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
