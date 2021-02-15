from django.shortcuts import get_object_or_404, render
from .basket import Basket
from store.models import Product
from django.http.response import JsonResponse


def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        response = JsonResponse({'test':'data'})
        return response