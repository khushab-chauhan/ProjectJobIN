# Generated by Django 5.2 on 2025-04-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='images',
            field=models.ImageField(blank=True, default='Default_Images/default.jpg', null=True, upload_to=''),
        ),
    ]
