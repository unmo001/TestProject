# Generated by Django 3.2.5 on 2021-07-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': '運営本部,フランチャイズ'},
        ),
        migrations.RenameField(
            model_name='access',
            old_name='kaeru_time',
            new_name='leave_time',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='honbu_flag',
            new_name='headquarters_flag',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='bikou',
            new_name='remarks',
        ),
        migrations.AddField(
            model_name='company',
            name='child_welfare_facility_flag',
            field=models.BooleanField(default=False, verbose_name='児童福祉施設'),
        ),
        migrations.AddField(
            model_name='company',
            name='franchise',
            field=models.BooleanField(default=False, verbose_name='フランチャイズ'),
        ),
    ]
