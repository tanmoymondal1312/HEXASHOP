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
    products = Product.objects.filter(is_available=True)  # Initialize with an empty queryset
    context = {}
    product_count = 0
    
    if request.method == 'POST':
        
        form = MyForm(request.POST)
        if form.is_valid():
            print('hello')
            field1_value = form.cleaned_data['field1']
            field2_value = form.cleaned_data['field2']
            field3_value = form.cleaned_data['field3']
            field4_value = form.cleaned_data['field4']
            
            print(field1_value)
            print(field2_value)
            print(field3_value)
            
            if field1_value !=None and field2_value !=None and field3_value != 'None' and field4_value != 'None':
                products = Product.objects.filter(is_available=True, price__range=(field1_value, field2_value),sizes=field3_value,color=field4_value)
                product_count = products.count()
                
            elif field1_value !=None and field2_value !=None and field3_value != 'None':
                products = Product.objects.filter(is_available=True, price__range=(field1_value, field2_value),sizes=field3_value)
                product_count = products.count()
                
            elif field1_value !=None and field2_value !=None:
                products = Product.objects.filter(is_available=True, price__range=(field1_value, field2_value))
                product_count = products.count()
            
        else:
            # Handle form validation errors here if needed
            pass
    else:
        # No form submission via POST, create an empty form
        form = MyForm()

    # Pagination code
    paginator = Paginator(products,3)
    page_number = request.GET.get("page",1)
    products = paginator.page(page_number)
    
    
    return render(request, 'filter_items.html', {'form': form, 'products':products})


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





