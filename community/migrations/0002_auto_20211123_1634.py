# Generated by Django 3.2.9 on 2021-11-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
