# Generated by Django 2.2 on 2019-04-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techs', '0002_auto_20190429_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='modelMaker',
        ),
        migrations.RemoveField(
            model_name='caryard',
            name='owner',
        ),
        migrations.DeleteModel(
            name='CarMaker',
        ),
        migrations.DeleteModel(
            name='CarModel',
        ),
        migrations.DeleteModel(
            name='CarYard',
        ),
    ]
