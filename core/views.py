from django.shortcuts import render
from core.models import Category,Product,Vendor,Product_Image,Product_Review,Wishlist,Address


def index(req):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(req,'core/index.html',context)
# Create your views here.
