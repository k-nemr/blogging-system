# Generated by Django 2.1 on 2018-08-04 09:48

from django.db import migrations


def create_data(apps, schema_editor):
    Blog = apps.get_model('blogs', 'Blog')
    Blog(author='Author 1', subject='Subject 1', body='Body 1').save()
    Blog(author='Author 2', subject='Subject 2', body='Body 2').save()


class Migration(migrations.Migration):
    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
