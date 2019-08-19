from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 继承AbstractUser
class TestUser(AbstractUser):
    # 真实姓名
    realname = models.CharField(max_length=8, verbose_name="真实姓名")
    # 手机号
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    # QQ号
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    # 个人头像
    avator_sor = models.ImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")