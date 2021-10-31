from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket


def basket(request):
    pass


def add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    basket_items = Basket.objects.filter(product=product_item, user=request.user).first()
    if not basket_items:
        basket_items = Basket(product=product_item, user=request.user)
    basket_items.quantity += 1
    basket_items.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove(request, pk):
    pass