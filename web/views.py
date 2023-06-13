from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login")
def index(request):
    context={
        "title":"Home Page"

    }
    return render(request,'web/index.html',context=context)
