from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.Singup , name='signup'),
    path('login',views.Login , name='login'),
    path('logout',views.Logout , name='logout'),
    path('profile',views.Profile , name='profile'),



    path('',views.Home , name='home'),
    path('productdetails/<int:id>',views.Productdetails , name='productdetails'),
    path('productcart',views.Product_cart , name='productcart'),
    path('productbuy',views.Product_Buy , name='productbuy'),
    path('cart',views.Show_cart , name='cart'),
    path('cart-plus',views.Plus_cart ),
    path('cart-minus',views.minus_cart ),
   
    path('cart-delete',views.delete_cart ),
    path('place-order',views.Place_order , name='place-order' ),
    path('order-done',views.Order_done , name='order-done' ),
    path('order',views.Order, name='order' ),

#    address delete and edit
    path('delete/<int:id>',views.Delete ,name='delete'),
    path('edit/<int:id>',views.CustomerEdit,name='edit'),

    # catagory and bran
    path('brand',views.Brands,name='brand'),
    path('catagory',views.Catagorydata,name='catagory'),

   # Seach
   # path('search',views.Search,name='search'),
   #customer review
   path('review',views.CustomerReview , name='review')
    

    
]
