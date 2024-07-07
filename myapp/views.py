from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Item
from .forms import Itemform 

# Create your views here.
def index(request):
    return HttpResponse("Home Page")
def item_list(request):
    items=Item.objects.all()
    return render(request,'itemlist.html',{'items':items})
def item_create(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('item_list')    
        else:
            form=Itemform()
    return render(request,'itemform.html',{'form':form})
