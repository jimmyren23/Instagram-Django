# Generated by Django 3.0.6 on 2020-06-01 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
