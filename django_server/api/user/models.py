from django.db import models
# from djongo import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(verbose_name='닉네임', max_length=255, default='', null=True, blank=True)
    nickname_used = models.BooleanField(verbose_name='닉네임사용여부', default=True, null=True, blank=True)
    phone_number = models.CharField(verbose_name='핸드폰번호', max_length=255, default='', null=True, blank=True)
    birth = models.DateField(verbose_name='생년월일', auto_created=False, auto_now=False, auto_now_add=False, default=None, null=True, blank=True)
    lunar = models.BooleanField(verbose_name='양력Y/음력N', default=True, null=True, blank=True)
    profile_img = models.URLField(verbose_name='프로필이미지', default='', null=True, blank=True)
    terms_agreed = models.BooleanField(verbose_name='필수법조항확인여부', default=False, null=True, blank=True)
    withdrawn = models.BooleanField(verbose_name='탈퇴여부', default=False, null=True, blank=True)
