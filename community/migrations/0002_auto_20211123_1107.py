# Generated by Django 3.2.9 on 2021-11-23 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='like_users',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie_title',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rank',
        ),
    ]