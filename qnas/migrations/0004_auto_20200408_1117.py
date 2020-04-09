# Generated by Django 2.2.5 on 2020-04-08 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_delete_thumbnail'),
        ('qnas', '0003_auto_20200408_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='item',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='items.Item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
