# Generated by Django 4.0.5 on 2022-06-26 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='roster',
        ),
    ]
