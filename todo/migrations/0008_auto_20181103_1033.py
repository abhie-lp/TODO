# Generated by Django 2.1.3 on 2018-11-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20181103_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=3),
        ),
    ]