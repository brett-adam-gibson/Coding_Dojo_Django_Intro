# Generated by Django 2.2 on 2020-07-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fav_books_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]