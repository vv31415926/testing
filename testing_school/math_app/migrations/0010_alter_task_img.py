# Generated by Django 3.2.9 on 2021-12-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0009_auto_20211202_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
