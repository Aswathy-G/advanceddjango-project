from django.shortcuts import render
def index(request):
    context={

    }
    return render(request,'web/index.html',context=context)
