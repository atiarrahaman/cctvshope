from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MegaPixel)
admin.site.register(Division)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['id','user','product','rating',]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','distric','division']


@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','productStatus']



@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display=['id','title']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['id','title']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=['id','color','color_code']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display=['id','size']

@admin.register(CcTvProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','catagory','color','size']

