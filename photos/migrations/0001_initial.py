# Generated by Django 3.1.2 on 2020-10-11 14:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('categorytags', models.ManyToManyField(to='photos.Category')),
                ('locationtags', models.ManyToManyField(to='photos.Location')),
            ],
        ),
    ]
