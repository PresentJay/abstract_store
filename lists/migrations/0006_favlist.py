# Generated by Django 2.2.5 on 2020-04-23 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200408_1145'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_auto_20200408_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(blank=True, related_name='lists', to='items.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
