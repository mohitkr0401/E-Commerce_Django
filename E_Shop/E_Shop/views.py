from django.shortcuts import redirect,render
from django.template.context_processors import request
from store_app.models import Product


def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    product = Product.objects.all()
    context = {
        'product':product,
    }
    return render(request, 'Main/index.html',context)