from django.contrib import admin
from .models import Product,Customer,Cart

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
  list_display = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']