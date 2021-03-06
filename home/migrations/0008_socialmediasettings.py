# Generated by Django 4.0.5 on 2022-06-29 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0007_homepage_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(help_text='Instagram username, without the @', max_length=255)),
                ('youtube', models.URLField(help_text='YouTube channel or user account URL')),
                ('spotify', models.URLField(help_text='Spotify account URL')),
                ('twitter', models.CharField(help_text='Twitter username, without the @', max_length=255)),
                ('tiktok', models.CharField(help_text='TikTok username, without the @', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
