# Generated by Django 2.1.3 on 2018-11-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_students_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='mobile',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
