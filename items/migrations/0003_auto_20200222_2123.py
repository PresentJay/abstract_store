# Generated by Django 2.2.5 on 2020-02-22 12:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200222_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
