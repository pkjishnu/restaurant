from django.shortcuts import render
from django.db.models import Q
from resto.models import Product

def searchresult(request):
    products=None
    if request.method=='POST':
        query=""
        query=request.POST.get('q')
        if query:
            products=Product.objects.filter(Q(name__icontains=query)|Q(desc__icontains=query));
        return render(request,'search.html',{'query':query,'p':products})
