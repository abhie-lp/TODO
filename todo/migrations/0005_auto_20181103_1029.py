# Generated by Django 2.1.3 on 2018-11-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181103_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default='1', max_length=1),
        ),
    ]
