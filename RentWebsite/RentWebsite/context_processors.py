"""
@file:context_processors.py
@author:李霞丹
@date：2019/08/20
"""
from django.shortcuts import reverse,redirect
from apps.accounts.forms import LoginForm
def login_data(request):
    login_form = LoginForm()
    current_url = request.path
    return locals()