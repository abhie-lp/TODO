# Generated by Django 2.1.3 on 2018-11-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], max_length=6),
        ),
    ]
