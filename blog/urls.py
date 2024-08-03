# copied from blogsite urls.py 

from django.urls import path
from blog import views

app_name= "blog"

urlpatterns = [
    path("",views.home,name='home'),
    path("article/by/category/<int:id>/",views.get_articlesbycategory,name='articlesbycateory'),
    path("article/detail/<int:id>/",views.get_article,name='get_article'),
        
]
