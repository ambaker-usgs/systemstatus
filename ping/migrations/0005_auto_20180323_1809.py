# Generated by Django 2.0.3 on 2018-03-23 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0004_auto_20180323_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hosts',
            options={'managed': False, 'verbose_name': 'Host entry', 'verbose_name_plural': 'Hosts entries'},
        ),
    ]
