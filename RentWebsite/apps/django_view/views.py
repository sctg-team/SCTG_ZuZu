from django.shortcuts import render,HttpResponse,redirect,Http404,get_object_or_404

# Create your views here.
# def test1(request):
#     raise Http404('not exist')
#     return HttpResponse('I am index')


def view_test(request):
    return HttpResponse('404.html')


