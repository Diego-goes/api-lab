# Generated by Django 4.2.4 on 2023-09-29 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reslab',
            name='res_date',
        ),
    ]
