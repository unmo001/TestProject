# Generated by Django 3.2.5 on 2021-07-16 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_report_is_public'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Report_Draft',
        ),
    ]
