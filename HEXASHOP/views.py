from django.shortcuts import render
from store.models import Product, Category, Reviews
from django.core.paginator import Paginator
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(products, 6)
    product_page = paginator.get_page(page)
    context = {"products": product_page, "categories": categories}
    return render(request, 'popular_products.html', context)


