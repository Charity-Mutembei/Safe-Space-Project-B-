# Generated by Django 4.1.3 on 2022-11-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joboapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]