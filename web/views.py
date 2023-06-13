from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage


from web.models import Product

@login_required(login_url="/users/login")
def index(request):
    products = Product.objects.filter(is_deleted=False,is_edit=False)
    instances = Paginator(products,6)
    page = request.GET.get('page',1)
    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)
    context={
        "title":"HomePage",
        "instances" : instances,
         
    }
    return render(request,'web/index.html',context=context)