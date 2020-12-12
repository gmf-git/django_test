from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class RoleModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='角色名称')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = "system_role"
        verbose_name = "角色表"


class UserModel(AbstractUser):
    first_name = None
    last_name = None
    last_login = None
    is_staff = None
    is_superuser = None
    name = models.CharField(max_length=255, verbose_name='姓名')
    role = models.ManyToManyField(RoleModel, verbose_name='角色')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'system_user'
        verbose_name = '用户表'
