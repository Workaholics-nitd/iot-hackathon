# Generated by Django 2.1.3 on 2019-11-19 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datavis', '0003_auto_20191119_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dustbin',
        ),
    ]