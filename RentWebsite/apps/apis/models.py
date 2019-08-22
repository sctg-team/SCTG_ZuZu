from django.db import models
from apps.accounts.models import User
from apps.goods.models import Goods
# Create your models here.


# 用户日志
class UserLog(models.Model):
    OPERATE = ((1, "收藏"), (2, "取消收藏"), (3, "租赁"))
    user = models.ForeignKey(User,verbose_name="用户")
    operate = models.CharField(choices=OPERATE, max_length=10,verbose_name="操作")
    good = models.ForeignKey(Goods, verbose_name="商品")
    create_time = models.DateTimeField(verbose_name="创造时间", auto_now_add=True)

    class Meta:
        verbose_name = "用户日志"
        verbose_name_plural = verbose_name
        ordering = ['-create_time',]

    def __str__(self):
        msg = ""
        if self.operate == 1:
            return "{}-{}-{}".format(self.user, self.operate,self.good)
        elif self.operate == 2:
            return "{}-{}-{}".format(self.user, self.operate, self.good)
        elif self.operate == 3:
            return "{}-{}-{}".format(self.user, self.operate, self.good)



# 评论表
# class