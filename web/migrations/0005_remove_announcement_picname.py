# Generated by Django 2.0.2 on 2018-06-23 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180623_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='picname',
        ),
    ]
