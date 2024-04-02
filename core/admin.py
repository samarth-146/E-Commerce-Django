from django.contrib import admin
from core.models import Category,Product,Product_Image,Product_Review,Cart,CartItem

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

class AdminCartOrder(admin.ModelAdmin):
    list_display=['user','is_paid']

class AdminOrderCartItem(admin.ModelAdmin):
    list_display=['cart','product']



admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Product_Review,AdminReview)
admin.site.register(Cart,AdminCartOrder)
admin.site.register(CartItem,AdminOrderCartItem)
# Register your models here.
