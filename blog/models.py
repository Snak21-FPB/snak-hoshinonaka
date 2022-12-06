from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class WriterManager(BaseUserManager):
    def create_user(self, username, email, permission=1, password=None):
        if not username:
            raise ValueError("Writer must have an username.")
        if not email:
            raise ValueError("Writer must have an email address.")

        user = self.model(
            username=username, email=self.normalize_email(email), permission=permission
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            permission=9,
        )
        user.save(using=self._db)
        return user


class Writer(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(verbose_name="ID", primary_key=True, unique=True)
    email = models.EmailField(verbose_name="メールアドレス", unique=True)
    password = models.CharField(verbose_name="パスワード", max_length=256)
    username = models.SlugField(verbose_name="ユーザー名", max_length=32, unique=True)
    name = models.CharField(verbose_name="名前", max_length=128, blank=True, null=True)
    permission = models.PositiveSmallIntegerField(verbose_name="権限", default=1)
    last_login = models.DateTimeField(verbose_name="最終ログイン日時", blank=True, null=True)
    login_num = models.IntegerField(verbose_name="ログイン回数", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WriterManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    @property
    def is_active(self):
        return self.permission >= 1

    @property
    def is_staff(self):
        return self.permission >= 2

    @property
    def is_superuser(self):
        return self.permission >= 9
