from django.shortcuts import render,get_object_or_404
from core.models import Category,Product,Product_Image,Product_Review,Cart,CartItem
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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


def product_detail_view(req,pid):
    product = get_object_or_404(Product, pid=pid)

    reviews=Product_Review.objects.filter(product=product)

    context={
        "product":product,
        "reviews":reviews,
    }
    return render(req,"core/product-details.html",context)

# views.py
def add_cart(req, pid):
    product = Product.objects.get(pid=pid)
    user =req.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_items = CartItem.objects.create(cart=cart, product=product)
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

@login_required
def view_cart(req):
    cartItem=CartItem.objects.all()
    context={
        "cartItem":cartItem
    }
    return render(req,'core/view_cart.html',context)

# Create your views here.
