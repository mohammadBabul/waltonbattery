# Generated by Django 3.0.4 on 2020-04-02 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='batterydataset',
            name='problem_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='battery.Category'),
            preserve_default=False,
        ),
    ]
