# Generated by Django 5.0.1 on 2024-02-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to='category'),
        ),
    ]
