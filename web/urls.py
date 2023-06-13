from django.urls import path,include
from web import views


app_name ="web" 

urlpatterns = [
    path('',views.index,name="index"),
    path("create/",views.create_product,name="create_product"),  

]