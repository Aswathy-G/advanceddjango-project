from django.urls import path
from web import views


app_name ="web" 

urlpatterns = [
    path('',views.index,name="index"),
    path("create/",views.create_product,name="create_product"), 
    path('deleted/<int:id>/',views.deleted_product,name="deleted_product"),
    path('edit/<int:id>/',views.edit_product,name="edit_product"),
    path('<int:id>/',views.product,name="product"),
]

