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
    path('product_detail/<pid>/',views.product_detail_view,name="product_detail"),
    path('add_to_cart/<str:pid>/',views.add_cart,name="add_cart"),
    path('view_cart/',views.view_cart,name="view_cart"),
] 