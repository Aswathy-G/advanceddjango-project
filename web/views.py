import json

from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from web.forms import ProductForm
from main.decorators import allow_self

from web.models import Product,Category,Price

@login_required(login_url="/users/login")
def index(request):
    products = Product.objects.filter(is_deleted=False,is_edit=False)
    categorys = Category.objects.all()
    prices = Price.objects.all()

    q = request.GET.get('q')
    if q:
        products = products.filter(title__istartswith=q)

    
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
        "categories" :categorys,
        "prices" : prices   
    }
    return render(request,'web/index.html',context=context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context={
                "title":"create page"

            }
            return HttpResponseRedirect(reverse('web:index'),context=context)
    else:
        form = ProductForm()

    return render(request, 'web/create.html', {'form': form})


@login_required(login_url="/users/login/")
@allow_self
def deleted_product(request,id):
    instance = get_object_or_404(Product,id=id)
    instance.is_deleted = True
    instance.save()

    response_data = {
        "title" : "Successfully deleted",
        "message" : "Post deleted successfully",
        "status" : "success"
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")


@login_required(login_url="/users/login/")
@allow_self
def edit_product(request,id):
    instance = get_object_or_404(Product,id=id)
    # print("first")
    if request.method == 'POST':
        # print("second")
        form = ProductForm(request.POST,request.FILES,instance=instance)
        

        if form.is_valid():
            instance = form.save(commit=False)
            # print("hai")
            instance.save()
            # return redirect('web/index.html')  # Redirect to the product list page
            return HttpResponseRedirect(reverse('web:index'))
    else:
        form = ProductForm(instance=instance)   

    return render(request, 'web/create.html', {'form': form})


def product(request,id):
    instance = get_object_or_404(Product.objects.filter(id=id))
    context = {
        "instance" : instance
        
    }
    return render(request, 'web/post.html',context=context)











