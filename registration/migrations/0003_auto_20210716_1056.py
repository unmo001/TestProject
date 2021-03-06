# Generated by Django 3.2.5 on 2021-07-16 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20210716_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='area',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='作業場所'),
        ),
        migrations.AlterField(
            model_name='report',
            name='insert_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='report',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='備考'),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='作業内容'),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='タイトル'),
        ),
        migrations.CreateModel(
            name='Report_Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('insert_time', models.DateTimeField(blank=True, null=True, verbose_name='日付')),
                ('area', models.CharField(blank=True, max_length=20, null=True, verbose_name='作業場所')),
                ('text', models.TextField(blank=True, null=True, verbose_name='作業内容')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='備考')),
                ('is_public', models.BooleanField(default=False, verbose_name='公開')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '日報下書き',
            },
        ),
    ]
