# Generated by Django 2.0.3 on 2018-03-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0005_auto_20180323_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('website_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000, verbose_name='Server hostname')),
                ('alias', models.CharField(blank=True, max_length=1000, verbose_name='Display name')),
                ('category', models.CharField(blank=True, max_length=1000, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'URL entries',
                'managed': False,
                'verbose_name': 'URL entry',
                'db_table': 'websites',
                'ordering': ['url'],
            },
        ),
        migrations.AlterModelOptions(
            name='hosts',
            options={'managed': False, 'ordering': ['host_name'], 'verbose_name': 'Host entry', 'verbose_name_plural': 'Hosts entries'},
        ),
        migrations.AlterModelTable(
            name='hosts',
            table='ping',
        ),
    ]
