from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Company(models.Model):
    company_name = models.CharField(verbose_name='会社名', max_length=50)
    honbu_flag = models.BooleanField(verbose_name='本部', default=False)

    class Meta:
        verbose_name_plural = "運営本部"

    def __str__(self):
        return self.company_name


class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name_plural = "ユーザー"


class Report(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル',max_length=30)
    insert_time = models.DateTimeField(verbose_name='日付',)
    area = models.CharField(verbose_name='作業場所', max_length=20)
    text = models.TextField(verbose_name='作業内容')
    bikou = models.TextField(verbose_name='備考')

    class Meta:
        verbose_name_plural = "日報"

    def __str__(self):
        return self.text


class Access(models.Model):
    user_name = models.CharField(verbose_name='利用者', max_length=20, null=False, blank=False)
    access_time = models.DateTimeField(verbose_name='入場', null=False, blank=False)
    kaeru_time = models.DateTimeField(verbose_name='退場', null=False, blank=False)

    class Meta:
        verbose_name_plural = "来客情報"

    def __str__(self):
        return self.user_name
