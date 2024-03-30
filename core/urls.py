from django.contrib import admin
from django.urls import path
from . import views
app_name='core'
urlpatterns = [
    path('',views.index,name='index'),
    path('category/',views.category_view,name="category"),
    path('products/',views.product_view,name="product"),
    path('category_product/<cid>/',views.category_product_view,name="category_product_view"),
    path('search/',views.search_product,name="search"),
    path('filter/',views.filtered_products,name="filtered_products"),
    path('product_detail/<pid>/',views.product_detail_view,name="product_detail"),
]   