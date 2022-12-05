from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class WriterManager(BaseUserManager):
    pass


class Writer(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(verbose_name="ID", primary_key=True, unique=True)
    email = models.EmailField(verbose_name="メールアドレス", unique=True)
    password = models.CharField(verbose_name="パスワード", max_length=256)
    username = models.SlugField(verbose_name="ユーザー名", max_length=32, unique=True)
    name = models.CharField(verbose_name="名前", max_length=128)
    permission = models.PositiveSmallIntegerField(verbose_name="権限", default=1)
    last_login = models.DateTimeField(verbose_name="最終ログイン日時", blank=True, null=True)
    login_num = models.IntegerField(verbose_name="ログイン回数", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
