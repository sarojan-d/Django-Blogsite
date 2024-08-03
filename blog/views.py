from django.shortcuts import render
from blog.models import category,Article

# Create your views here.

def home(request):
    categories = category.objects.all()
    articles = Article.objects.all()
    context = {'categories':categories,'articles':articles}
    return render(request,'index.html',context)

def get_articlesbycategory(request,id):
    categories = category.objects.all()
    cat = category.objects.get(id=id)
    article= Article.objects.filter(category_id=cat)
    # print(article)
    context={'cat':cat,'articles':article,'categories':categories}
    return render(request,'articlelist.html',context)

def get_article(request,id):
    categories = category.objects.all()
    article = Article.objects.get(id=id)
    context={'article':article,'categories':categories}
    return render(request,'articledetail.html',context)
