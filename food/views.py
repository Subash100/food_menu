from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Item
from .forms import ItemForm
# Create your views here.
# def index(request):
#     item_list = Item.objects.all()
#     context={
#         'item_list': item_list,
#     }
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context='item_list'

# def detail(request,id):
#     item=Item.objects.get(pk=id)
#     return render(request,'food/detail.html',{'item':item})

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context='item'


class CreateItem(CreateView):
    model = Item
    template_name = 'food/item-form.html'
    fields = ['item_name','item_desc','item_price','item_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})

def update_item(request,id):
    item=Item.objects.get(pk=id)
    form=ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form': form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item': item})



