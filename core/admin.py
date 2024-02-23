from django.contrib import admin
from core.models import Category,Product,Vendor,Product_Image,Product_Review,Wishlist,Address

class ProductImage(admin.TabularInline):
    model=Product_Image

class AdminCategory(admin.ModelAdmin):
    list_display=['title','image']
    
class AdminProduct(admin.ModelAdmin):
    inlines=[ProductImage]
    list_display=['title','user','price','image','in_stock']

class AdminVendor(admin.ModelAdmin):
    list_display=['title','user','image','rating','contact_number']

class AdminReview(admin.ModelAdmin):
    list_display=['user','review_stars','date','review_description']

class AdminWishlist(admin.ModelAdmin):
    list_display=['user','wish_date']

class AdminAddress(admin.ModelAdmin):
    list_display=['user','address']

admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Vendor,AdminVendor)
admin.site.register(Product_Review,AdminReview)
admin.site.register(Wishlist,AdminWishlist)
admin.site.register(Address,AdminAddress)
# Register your models here.
