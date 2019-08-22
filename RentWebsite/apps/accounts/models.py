from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.fields.files import ImageFieldFile
from libs.images import make_thumb
from RentWebsite.context_processors import valid_sex
from RentWebsite.settings import MEDIA_ROOT, THUMB_SIZE
import os

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


# 用户表
class UserInfo(AbstractUser):
    SEX_CHOICES = ((None, "请选择"),
                    (0, "男"),
                    (1, "女"),
                    )
    realname = models.CharField(max_length=8, verbose_name="真实姓名")  # 需要出租或承租就需要完善本字段
    sex = models.IntegerField("性别", choices=SEX_CHOICES,validators=[valid_sex])
    mobile = models.CharField(max_length=11, verbose_name="手机号")  # 需要出租或承租就需要完善本字段
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    id_card = models.CharField(max_length=18, verbose_name="身份证号")  # 需要出租或承租就需要完善本字段
    address = models.CharField(verbose_name="地址")
    avator_sor = ThumbnailerImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")
    avator_sm = models.ImageField('头像缩略图', upload_to='avator/%Y%m%d/', default='avator/5.70x70.jpg')

    def save(self, *args, **kwargs):
        # 将上传的图片先保存
        super().save()
        # 　如果是默认图片不压缩
        if self.avator_sor.name == 'avator/default.jpg':
            return
        # 如果文件不存在，不压缩
        if not os.path.exists(os.path.join(MEDIA_ROOT, self.avator_sor.name)):
            return

        base, ext = os.path.splitext(self.avator_sor.name)
        # 从头像中生成缩略图
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.avator_sor.name), size=THUMB_SIZE)

        if thumb_pixbuf:
            # 缩略图的保存文件全路径=> 保存文件
            thumb_path = os.path.join(MEDIA_ROOT, base + '.{}x{}'.format(THUMB_SIZE, THUMB_SIZE) + ext)
            # 缩略图相对路径 => 数据库(以下两种取相对路径都可)
            relate_thumb_path = os.path.join('/'.join(self.avator_sor.name.split('/')[:-1]),
                                             os.path.basename(thumb_path))
            relate_thumb_path = base + '.{}x{}'.format(THUMB_SIZE, THUMB_SIZE) + ext
            # 保存缩略图
            thumb_pixbuf.save(thumb_path)
            # 保存字段值
            self.avator_sm = ImageFieldFile(self, self.avator_sm, relate_thumb_path)
            super().save()  # 再保存一下，包括缩略图等


