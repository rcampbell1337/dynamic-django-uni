# Generated by Django 3.1.5 on 2021-01-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
    ]
