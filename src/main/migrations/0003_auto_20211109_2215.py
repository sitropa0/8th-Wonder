# Generated by Django 3.1.7 on 2021-11-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211107_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='currentHole',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='hole',
            field=models.IntegerField(default=0),
        ),
    ]
