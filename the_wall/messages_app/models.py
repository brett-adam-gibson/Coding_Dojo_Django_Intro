from django.db import models
from users_app.models import User

# Create your models here.
class PostManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        #title has to not be empty
        if len(post_data['title']) < 1:
            errors['title'] = 'title was to short.'
        if len(post_data['content']) < 5:
            errors['content'] = 'post needs to be atleast 5 characters.'
        return errors

class CommentManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['comment_content']) < 5:
            errors['comment_content'] = 'comment needs to be atleast 5 characters.'
        return errors

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    objects = PostManager()
#   Post.author = User

class Comment(models.Model):
    comment_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post_message = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')

    objects = CommentManager()
