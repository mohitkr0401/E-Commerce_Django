from django.shortcuts import redirect,render
from django.template.context_processors import request


def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    return render(request, 'Main/index.html')