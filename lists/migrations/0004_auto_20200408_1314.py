# Generated by Django 2.2.5 on 2020-04-08 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200408_1145'),
        ('lists', '0003_auto_20200408_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='option',
        ),
        migrations.AddField(
            model_name='orderlist',
            name='option',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orderlists', to='items.Option'),
            preserve_default=False,
        ),
    ]
