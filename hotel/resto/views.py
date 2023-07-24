from django.shortcuts import render
from resto.models import Category,Product
from cart.models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
def allproducts(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def viewproducts(request,cslug):
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)
    return render(request,'products.html',{'p':p,'c':c})
def prodetail(request,pslug):
    c=Category.objects.all()

    p=Product.objects.get(slug=pslug)
    return render(request,'detail.html',{'p':p,'c':c})
def user_login(request):
    if (request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allproducts(request)
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return allproducts(request)

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p == cp:
            user = User.objects.create_user(username=u, first_name=f, last_name=l, email=e, password=p)
            user.save()
            return allproducts(request)
    return render(request, 'register.html')
def customer(request):
    user=request.user
    a=Account.objects.get(user=user)

    return render(request,'customer.html',{'a':a})




