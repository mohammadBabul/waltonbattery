# Generated by Django 3.0.4 on 2020-04-03 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0003_batterydataset_problem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batterydataset',
            name='problem_category',
        ),
    ]