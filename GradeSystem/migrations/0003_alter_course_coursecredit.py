# Generated by Django 3.2.9 on 2021-11-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeSystem', '0002_alter_course_coursedescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseCredit',
            field=models.IntegerField(),
        ),
    ]