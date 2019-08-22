from django.db import models
from apps.accounts.models import User
from apps.goods.models import Goods,Category



# Create your models here.

# 租赁-记录表
class Lease(models.Model):
    # 出租人
    lor = models.ForeignKey(User, verbose_name="出租人",related_name="lor")
    # 承租人
    lee = models.ForeignKey(User, verbose_name="承租人",related_name="lee")
    # 出租物品
    goods = models.ForeignKey(Goods, verbose_name="出租物品",related_name="g_name")
    # 开始时间
    s_time = models.DateTimeField(verbose_name="开始时间",auto_now_add=True)
    # 最后一次修改时间
    last_modify = models.DateTimeField(auto_now=True)
    # 租金
    rent = models.ForeignKey(Goods,verbose_name="租金",related_name="rents")

    #
    class Meta:
        verbose_name = "租赁记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 什么时候谁租了谁的什么东西
        return "{}---{}租了{}的{}".format(self.s_time,self.lee,self.lor,self.goods)






