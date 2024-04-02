from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


RATING=(
    (1, '★ ☆ ☆ ☆ ☆'),
    (2,'★ ★ ☆ ☆ ☆'),
    (3,'★ ★ ★ ☆ ☆'),
    (4,'★ ★ ★ ★ ☆'),
    (5,'★ ★ ★ ★ ★')
)

ORDER_STATUS=(
    ('pending','Pending'),
    ('processing','Processing'),
    ('completed','Completed')
)

def user_directory_path(instance, filename): 
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Category(models.Model):
    cid=ShortUUIDField(unique=True,max_length=20,length=10,prefix='cat',alphabet="abcdefgh12345")
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="category",default='1.jpg')

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'%(self.image.url))
    def __str__(self):
        return self.title

# class Vendor(models.Model):
#     vid=ShortUUIDField(unique=True,max_length=20,length=10,prefix='ven',alphabet="abcdefgh12345")
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     image=models.ImageField(upload_to=user_directory_path)

#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     contact_number=models.CharField(max_length=15,default=+911234567890)
#     address=models.CharField(max_length=100)
#     days_return=models.CharField(max_length=100)
#     rating=models.CharField(max_length=100,default=100)
#     resp_time=models.CharField(max_length=100)
#     warranty_period=models.CharField(max_length=100)

#     def vendor_image(self):
#         return mark_safe('<img src="%s" width="50" height="50"/>'%self.image.url)
#     def __str__(self):
#         return self.title


class Product(models.Model):
    pid=ShortUUIDField(unique=True,max_length=20,length=10,prefix='pro',alphabet='abcdefgh12345')
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to=user_directory_path,default="")
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=9999999,decimal_places=2,default=100)
    old_price=models.DecimalField(max_digits=9999999,decimal_places=2,default=150)
    specifications=models.TextField(null=True,blank=True)
    in_stock=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)
    def discount(self):
        discount_per=100-(self.price/self.old_price)*100
        return discount_per
    # product_rates=models.CharField(choices=RATING,max_length=100)


    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>'%(self.image.url))
    def __str__(self):
        return self.title

class Product_Image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product-image")
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        if self.product:
            return self.product.title
        else:
            return "CartItem without Product"





class Product_Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    review_description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    review_stars=models.IntegerField(choices=RATING)

    def __str__(self):
        if self.product:
            return self.product.title
        else:
            return "Product Review (No Product)"




# Create your models here.
