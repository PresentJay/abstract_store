# Generated by Django 2.2.5 on 2020-04-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20200408_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
