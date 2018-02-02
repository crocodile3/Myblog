from django.shortcuts import render
from django.http import HttpResponse,Http404
from blog.models import Blog
from datetime import *
# Create your views here.



def detail(request, id):
    try:
        post = Blog.objects.get(id = str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})
def home(request):
    post_list = Blog.objects.all()
    return render(request,"blog/home.html",{'post_list' : post_list})

def main_page(request):
    post_list = Blog.objects.all()  #获取全部的Article对象
    return render(request, 'blog/base.html', {'post_list' : post_list})


