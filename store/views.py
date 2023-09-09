from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Reviews
from django.urls import reverse
from django.contrib import messages
from category.models import Category
from django.core.paginator import Paginator
from .forms import MyForm,ReviewModelForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        # Filter products by category if category_slug is provided
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category).order_by('product_name')
    else:
        # No category_slug provided, filter all available products
        products = Product.objects.filter(is_available=True).order_by('product_name')

    # Paginate the products
    page = request.GET.get("page")
    paginator = Paginator(products, 4)
    product_page = paginator.get_page(page)
    categories = Category.objects.all()
    context = {"products": product_page, "categories": categories}
    return render(request, "store.html", context)





@csrf_exempt
def FilterItems(request):
    products = Product.objects.filter(is_available=True)

    min_price = request.GET.get('field1')
    max_price = request.GET.get('field2')
    size = request.GET.get('field3')
    color = request.GET.get('field4')

    # Create an empty Q object to combine filter conditions
    filter_conditions = Q()

    if min_price:
        filter_conditions &= Q(price__gte=float(min_price))

    if max_price:
        filter_conditions &= Q(price__lte=float(max_price))

    if size and size != 'None':
        filter_conditions &= Q(sizes=size)

    if color and color != 'None':
        filter_conditions &= Q(color=color)

    print(filter_conditions)

    # Apply the filter conditions
    products = products.filter(filter_conditions)

    form = MyForm()
    product_count = products.count()

    # Pagination code
    paginator = Paginator(products, 3)
    page_number = request.GET.get("page", 1)
    products = paginator.page(page_number)

    context = {
        'form': form,
        'products': products,
        'p_count': product_count,
        'field1': min_price,
        'field2': max_price,
        'field3': size,
        'field4': color
    }

    return render(request, 'filter_items.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.filter(product=product)
    
    average_rating = 0 
    
    if reviews.exists():
        total_rating = sum([review.rating for review in reviews])
        average_rating = total_rating / len(reviews)

    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product_id)
    
    
    else:
        form = ReviewModelForm()
    

    return render(request, 'product_detail.html', {'average_rating':average_rating,'reviews':reviews,'product': product, 'form': form})





