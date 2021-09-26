# Generated by Django 3.2.6 on 2021-08-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('category_image', models.ImageField(blank=True, upload_to='Static/images/categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
