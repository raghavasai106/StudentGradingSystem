# Generated by Django 3.2.9 on 2021-11-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeSystem', '0008_auto_20211111_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[('Student', 'Student'), ('Instructor', 'Instructor')]),
        ),
    ]