# Generated by Django 3.0.6 on 2020-05-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200528_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Completed'), (1, 'Not Completed')], default=0),
        ),
    ]