from django.shortcuts import render
from djangoapp.models import Post

# Create your views here.
def post(request):
    posts=Post.objects.all()
    contex={
        'post':posts
        
        }
    
    return render(request,'djangoapp/index.html',contex)

def detail(request,pk):
    detail=Post.objects.get(pk=pk)

    context_one={
        'single_post':detail
    }
    return render(request,'djangoapp/detail.html',context_one)

def navbar(request):
    return render(request,'djangoapp/base.html')

def gallery(request):
    return render(request,'djangoapp/gallery.html')

def contact(request):
    return render(request,'djangoapp/contact.html')