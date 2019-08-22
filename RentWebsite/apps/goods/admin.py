from django.contrib import admin
from . import models

# Register your models here.
# 手动
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Goods)