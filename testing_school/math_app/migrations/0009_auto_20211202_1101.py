# Generated by Django 3.2.9 on 2021-12-02 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0008_alter_lesson_correctly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='math_app.student'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='math_app.task'),
        ),
        migrations.AlterField(
            model_name='version',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='math_app.task'),
        ),
    ]
