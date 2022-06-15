from django.shortcuts import redirect, render
from product.forms import ProductAdd

from product.models import ProductA, ProductB
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
def home_page(request):
    try:
        product = ProductA.objects.all()
        paginator = Paginator(product, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except:
        raise Http404  
    return render(request, 'home.html', {'page_obj': page_obj})


def add_product(request):
    if request.method == 'POST':
        form = ProductAdd(request.POST)
        if form.is_valid():          
            form.save()
            return redirect('home')
    else:
        form = ProductAdd()
    return render(request, 'add_product.html', {'form': form})