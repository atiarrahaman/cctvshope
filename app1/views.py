from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def Login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request.POST,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        fm=AuthenticationForm()
    context={'form':fm}
    return render(request,'login.html',context)


def Logout(request):
  logout(request)
  return redirect('login')

def Singup(request):
    if request.method == 'POST':
        fm=Singupform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm=Singupform()
    context={'form':fm}
    return render(request,'signup.html',context)


def Profile(request):
    if request.user.is_authenticated:
        add=Customer.objects.filter(user=request.user)
        if  request.method== 'POST':
            fm=AdressForm(request.POST)
            if fm.is_valid():
                fm = fm.save(commit=False)
                fm.user=request.user
                fm=fm.save()
                fm=AdressForm()
                
        else:
            fm=AdressForm()
        context={'form':fm,'add':add}
        return render(request,'profile.html',context)
    else:
        return redirect('login')



def Home(request):
    data= CcTvProduct.objects.all().order_by('-id')

    context={'data':data,}
    return render(request,'home.html',context)


def Productdetails(request,id):
    product=CcTvProduct.objects.get(id=id)
    item_already_have=False
    if request.user.is_authenticated:
        
        item_already_have=Cart.objects.filter(Q(user=request.user) & Q (product=product.id)).exists()
    context={'product':product,'item_already_have':item_already_have}
    return render(request,'productdetails.html',context)

@login_required 
def Product_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    products=CcTvProduct.objects.get(id=product_id)
    
    Cart(user=user,product=products).save()
    return redirect('cart')

@login_required 
def Product_Buy(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    products=CcTvProduct.objects.get(id=product_id)
    
    Cart(user=user,product=products).save()
    return redirect('place-order')



def Show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user).order_by('-id')
        amount=0.0
        shipinamounnt=20.0
        totalamount=0.0
        product_cart=[p for p in Cart.objects.all() if p.user == user]
        if product_cart:
            for p in product_cart:
                tempamount=(p.quantity * p.product.price)
                amount+=tempamount
                totalamount= amount+shipinamounnt
        context={'carts':cart,'totalamount':totalamount,'amount':amount,}
        return render(request,'productcart.html',context)
    else:
        return redirect('login')


@login_required 
def Plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipingamount=20
        
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in  cart_product:
            tempamount=(p.quantity*p.product.price)
            amount+=tempamount
          
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipingamount

        }
        return JsonResponse(data)

@login_required 
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        print(prod_id)
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipingamount=20
        
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in  cart_product:
            tempamount=(p.quantity*p.product.price)
            amount+=tempamount
            
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipingamount

        }
        return JsonResponse(data)


@login_required 
def delete_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
       
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        
        c.delete()
        amount=0.0
        shipingamount=20
        
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in  cart_product:
            tempamount=(p.quantity*p.product.price)
            amount+=tempamount
            
        data={
           
            'amount':amount,
            'totalamount':amount+shipingamount

        }
        return JsonResponse(data)

@login_required    
def Place_order(request):
    add=Customer.objects.filter(user=request.user)
    order_place=Cart.objects.filter(user=request.user)
    amount=0.0
    shipping=20.0
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
    for p in  cart_product:
        tempamount=(p.quantity*p.product.price)
        amount+=tempamount
    totalamount=amount+shipping  
    
    if  request.method== 'POST':
        fm=AdressForm(request.POST)
        if fm.is_valid():
            fm = fm.save(commit=False)
            fm.user=request.user
            fm=fm.save()
            fm=AdressForm()
            
    else:
        fm=AdressForm()     
    context={'add':add,
             'order_place':order_place,
             'totalamount':totalamount,
            'form':fm,
             }
    return render(request,'placeorder.html',context)

@login_required 
def CustomerEdit(request,id):
    ed=Customer.objects.get(id=id)
    if request.method== 'POST':
        fm=AdressForm(request.POST,instance=ed)
        if fm.is_valid():
            fm.save()
            return redirect('place-order')
    else:
        fm=AdressForm(instance=ed)
    context={'forms':fm}
    return render(request,'editaddress.html',context)
        
def Delete(request,id):
    dl=Customer.objects.get(id=id)
    dl.delete()
    return redirect('place-order')

@login_required 
def Order_done(request):
    address=request.GET.get('adid')
    ad=Customer.objects.get(id=address)
    cart=Cart.objects.filter(user=request.user)
    for c  in cart:
        PlaceOrder(user=request.user ,customer=ad ,product=c.product,quantity=c.quantity ).save()
        c.delete()
    return redirect('order')


@login_required 
def Order(request):
    order=PlaceOrder.objects.filter(user=request.user).order_by('-id')
    context={'order':order}
    return render(request,'order.html',context)