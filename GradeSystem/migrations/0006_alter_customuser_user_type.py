# Generated by Django 3.2.9 on 2021-11-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeSystem', '0005_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'Instructor'), (2, 'Student')], default=1, max_length=10),
        ),
    ]
