# Generated by Django 4.0.5 on 2022-07-04 09:28

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0011_homepagecarouselimages_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='from_address',
            field=models.EmailField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='thank_you_text',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='spotify',
            field=models.URLField(help_text='Spotify account or playlist URL'),
        ),
        migrations.CreateModel(
            name='SocialImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link', models.URLField(blank=True, default='')),
                ('name', models.CharField(help_text='Social platform', max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_images', to='home.homepage')),
                ('social_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
