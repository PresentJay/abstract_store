# Generated by Django 2.2.5 on 2020-03-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=1024)),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('delivery_status', models.CharField(choices=[('Preparing for delivery', 'Preparing for delivery'), ('Shipping', 'Shipping'), ('Delivery completed', 'Delivery completed'), ('Canceled', 'Canceled')], default='Preparing for delivery', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=1024)),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=1024)),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('option', models.ManyToManyField(blank=True, related_name='wishlists', to='items.Option')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
