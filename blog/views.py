from django.shortcuts import render

# Create your views here.
from .models import Category, Post


def index(request):
    post_list = Post.objects.all()   # 查询到所有的文章
    context = {'post_list': post_list }
    return render(request, 'blog/index.html', context)