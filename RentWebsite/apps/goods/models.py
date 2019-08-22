from django.db import models
# from django.core.exceptions import ValidationError
# from RentWebsite.context_processors import valid_difficulty
# from ckeditor.fields import RichTextField
# 包含文件上传
from ckeditor_uploader.fields import RichTextUploadingField
from apps.accounts.models import User

# Create your models here.

# 商品分类
class Category(models.Model):
    """分类"""
    name = models.CharField("分类名称", max_length=64)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)


# 商品标签
class Tag(models.Model):
    """标签"""
    name = models.CharField("标签名", max_length=64)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)


# 商品表
class Goods(models.Model):
    """商品库"""
    # DIF_CHOICES = (
    #     (1, ""),
    #     (2, "简单"),
    #     (3, "中等"),
    #     (4, "困难"),
    #     (5, "超难"),
    # )
    # grade = models.IntegerField("题目难度", choices=DIF_CHOICES, validators=[valid_difficulty], null=True)
    category = models.ForeignKey(Category, verbose_name="所属分类")
    title = models.CharField("商品标题", max_length=256)
    # 富文本编辑器
    # g_name = RichTextUploadingField("物品名称", null=True)
    # 富文本编辑器
    desc = RichTextUploadingField("物品描述", null=True, blank=True)
    # 租金
    rent = models.DecimalField("租金",max_digits=11,decimal_places=10)
    # 押金
    deposit = models.DecimalField("押金",max_digits=11,decimal_places=10)
    # 出租人
    user = models.ForeignKey(User, verbose_name="贡献者")
    pub_time = models.DateTimeField("入库时间", auto_now_add=True)
    # 审核状态
    status = models.BooleanField("审核状态", default=False)
    # 数组....(会产生一个中间表)
    tag = models.ManyToManyField(Tag, verbose_name="商品标签")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        # 定义权限=>auth_permission表插入数据
        permissions = (
            ('can_change_good', "可以修改商品信息"),
            ('can_add_good', "可以添加商品信息"),
            ('can_change_good_status', "可以修改商品状态"),
        )

    def __str__(self):
        return "{}:{}".format(self.id, self.title)


# 商品收藏表
class GoodsCollection(models.Model):
    goods = models.ForeignKey(Goods,verbose_name="出租物品",related_name='goods_collection_set')
    user = models.ForeignKey(User,verbose_name="收藏者",related_name='goods_collection_set')
    create_time = models.DateTimeField("收藏/取消时间", auto_now=True)
    # True表示收藏，False表示未收藏
    status = models.BooleanField("收藏状态",default=True)

    class Meta:
        verbose_name = "收藏记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status:
            ret = "收藏"
        else:
            ret = "取消收藏"
        return "{}:{}:{}".format(self.user,ret,self.goods.title)





