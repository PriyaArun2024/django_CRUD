from django.shortcuts import render,redirect,get_object_or_404

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
def item_delete(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('item_list')
    return redirect(request,'itemconfirmdelete.html',{'item':item})

