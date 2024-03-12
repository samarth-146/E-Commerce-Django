from django.shortcuts import render
from core.models import Category,Product,Vendor,Product_Image,Product_Review,Wishlist,Address


def index(req):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        "products":products,
        "categories":categories,
    }
    return render(req,'core/Amazon.html',context)

def category_view(req):
    categories=Category.objects.all()
    context={
        "categories":categories
    }
    return render(req,"core/category_view.html",context)
# Create your views here.
