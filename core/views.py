from django.shortcuts import render,get_object_or_404
from core.models import Category,Product,Vendor,Product_Image,Product_Review,Wishlist,Address


def index(req):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        "products":products,
        "categories":categories,
    }
    return render(req,'core/newindex.html',context)

def category_view(req):
    categories=Category.objects.all()
    context={
        "categories":categories
    }
    return render(req,"core/category_view.html",context)

def product_view(req):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        "products":products,
        "categories":categories,
    }
    return render(req,"core/product_view.html",context)

def category_product_view(req,cid):
    category=Category.objects.get(cid=cid)
    product=Product.objects.filter(category=category)
    categories=Category.objects.all()
    context={
        "category":category,
        "product":product,
        "categories":categories
    }
    return render(req,"core/category_product.html",context)


def search_product(req):
    query=req.GET.get("q")
    products = Product.objects.filter(title__icontains=query)
    categories=Category.objects.all()
    context={
        "products":products,
        "query":query,
        "categories":categories
    }
    return render(req,"core/search.html",context)

def filtered_products(request):
    selected_categories = request.GET.getlist('category')
    selected_price_ranges = request.GET.getlist('price_range')

    filtered_products = Product.objects.all()

    if selected_categories:
        filtered_products = filtered_products.filter(category__in=selected_categories)
    
    if selected_price_ranges:
        price_ranges = [price_range.split('-') for price_range in selected_price_ranges]
        for price_range in price_ranges:
            filtered_products = filtered_products.filter(price__gte=price_range[0], price__lte=price_range[1])

    return render(request, 'core/filtered_products.html', {'filtered_products': filtered_products})

def product_detail_view(req,pid):
    product = get_object_or_404(Product, pid=pid)
    context={
        "product":product
    }
    return render(req,"core/product-details.html",context)
# Create your views here.
