from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    def validator(self, postdata):
        errors = {}
        if len(postdata['comment']) < 5:
            errors['comment'] = "Comment must be at least 5 characters"
        return errors

class CourseManager(models.Manager):
    def validator(self, postdata):
        errors = {}
        if len(postdata['name']) < 5:
            errors['name'] = 'Course name must be at least 5 characters long.'
        if len(postdata['description']) < 15:
            errors['description'] = 'Description must be at least 15 characters long.'
        return errors

class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.OneToOneField(
        Description, related_name="course", null=True, on_delete=models.CASCADE)

    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
