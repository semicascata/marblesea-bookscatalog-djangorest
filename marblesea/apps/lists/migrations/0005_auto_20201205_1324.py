# Generated by Django 3.1.3 on 2020-12-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20201203_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]