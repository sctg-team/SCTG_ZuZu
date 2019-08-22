from django.shortcuts import render
from django.views.generic import View
from apps.goods.models import Goods,Category


# Create your views here.
class GoodsList(View):
    def get(self, request):
        category = Category.objects.all()
        grades = Goods.DIF_CHOICES
        # 添加search参数，以便搜索刷新后在页面上还能看到搜索的关键字
        search = request.GET.get("search","")
        kwgs = {"category":category,
                "grades":grades,
                "search_key":search,
                }
        return  render(request, "repo/index2.html", kwgs)