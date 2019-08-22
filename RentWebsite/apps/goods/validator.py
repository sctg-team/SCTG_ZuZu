"""
@file:validator.py
@date:2019/08/22
"""

from django.core.exceptions import ValidationError

# 商品分类的程度
def valid_difficulty(n):
    n = int(n)
    if n > 5 or n <1:
        raise ValidationError("难度介于1到5之间")

def valid_sex(n):
    n = int(n)
    if n>2 or n < 0:
        raise valid_difficulty("性别只有男or女,可以选择隐藏")